# TODO Fix and Test

import random
import string
import time
import zipfile
from os import path, listdir, remove, rmdir
from threading import Thread
import file_manager as fm
import traceback


class RandomKeyGenerator(object):
    days = 0.00138888888

    def __init__(self, exp_dur, code_len):
        self.codes = []
        self.exp_dur = exp_dur
        self.days = float(exp_dur) / 86400
        self.code_len = code_len

    def generate_code(self):
        c = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(self.code_len))
        if c in [k[0] for k in self.codes]:
            return self.generate_code()
        x = [c, time.time() + self.exp_dur]
        self.codes.append(x)
        return x

    def remove(self, code):
        self.codes.remove(code)

    def update(self):
        to_delete = []
        codes = self.codes
        for i in range(len(codes)):
            if codes[i][1] <= time.time():
                to_delete.append(i)
        deleted = [codes[i] for i in range(len(codes))[::-1] if i in to_delete]
        for i in to_delete:
            del codes[i]
        return deleted


class OnlineFileManager(object):
    sleep_secs = 5

    def __init__(self, rkg):
        self.files = {}
        self.rkg = rkg
        self.temp_folders = []
        self.thread = Thread(target=OnlineFileManager.thread_run, args=(self,))
        self.thread.start()

    def add_file(self, file):
        c = self.rkg.generate_code()
        try:
            self.files.update({tuple(c): file})
        except BaseException, ex:
            print ex
        print self.files
        return c

    def get_file(self, code):
        if tuple(code) in self.files:
            i = [g for g in range(len(self.files.keys())) if self.files.keys()[g] == tuple(code)][0]
            zip_file = zipfile.ZipFile(self.files.values()[i])
            return [zip_file, self.files.items()[i]]

    def unzip_to_tmp(self, zip_file):
        zf = zip_file[0]
        f = zip_file[1]
        unique = False
        rnd = 0
        while not unique:
            rnd = random.randint(0, fm.temp_range)
            if rnd not in self.temp_folders:
                unique = True
        folder_string = ''
        if rnd == 0:
            folder_string = '00'
        else:
            folder_string = str(rnd)
        pth = path.join(fm.temp_folder, ('temp' + folder_string))
        self.temp_folders.append([f, pth])
        zf.extractall(pth)
        return pth

    def clear_temp(self, temp_folder):
        for fn in listdir(temp_folder[1]):
            remove(path.join(temp_folder[1], fn))
        rmdir(temp_folder[1])

    def clear_temp_by_code(self, code):
        pth = [temp_folder[1] for temp_folder in self.temp_folders if temp_folder[0][0][0] == code][0]
        for fn in listdir(pth):
            remove(path.join(pth, fn))
        rmdir(pth)

    def update(self):
        temp_to_delete = []
        tf = self.temp_folders
        for i in range(len(tf)):
            if tf[i][0][0][1] <= time.time():
                temp_to_delete.append(i)
        temp_deleted = [tf[i] for i in range(len(tf)) if i in temp_to_delete]
        for i in temp_to_delete[::-1]:
            del tf[i]
        files = self.files
        files_to_delete = [k for k, v in files.items()[::-1] if k[1] <= time.time()]
        for k in files_to_delete:
            del files[k]
        return temp_deleted

    def thread_run(self):
        try:
            while self.thread.isAlive():
                t = time.time()
                dfs = self.update()
                for df in dfs:
                    self.clear_temp(df)
                u = self.rkg.update()
                time_elapsed = time.time() - t
                print self.files
                time.sleep(OnlineFileManager.sleep_secs - time_elapsed)
        except:
            traceback.print_exc()
