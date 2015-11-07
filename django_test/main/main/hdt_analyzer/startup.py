from core.online_file_manager import OnlineFileManager, RandomKeyGenerator
ofm = None
def init():
    global ofm
    ofm = OnlineFileManager(RandomKeyGenerator(60, 1))
    print 'check'