import json

class TestAPI():
    def test_root_page(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'drinking from Flask!'

    def test_get_dad_jokes(self, api):
        res = api.get('/dadjokes')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_post_dad_jokes(self, api):
        mock_data = json.dumps({'joke': 'test joke'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/dadjokes', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_bad_path(self, api):
        res = api.get('/jim')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']
