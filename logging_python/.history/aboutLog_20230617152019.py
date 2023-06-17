import logging


# logging 객체 선언
logger = logging.getLogger()


'''
log로 기록 될 레벨 선정
    ex) 여기선 INFO 레벨 이상부터 모든 LOG가 기록된다
'''
logger.setLevel(logging.INFO)


'''
log가 기록 될 형식 지정
언급했던 내용처럼 시간, 로그 레벨, 메시지(해당 작업에 대한 코멘트)
'''
formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')

'''
log file을 저장할 경로와 encoding 형식 지정
'''
file_handler = logging.FileHandler('LogPractice.log', encoding='utf-8')

'''

'''
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


logger.info('logging 입력 test\n')









