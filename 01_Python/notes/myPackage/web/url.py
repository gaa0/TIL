def my_url(itemPerPage=10, **api):
    if itemPerPage<1 or itemPerPage>10:
        return '1~10까지의 값을 넣어주세요.'
    else:
        if 'key' in api and 'targetDt' in api:
            return f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?itemPerPage={itemPerPage}&key={api.get("key")}&targetDt={api.get("targetDt")}&'
        else:
            return '필수 요청변수가 누락되었습니다.'