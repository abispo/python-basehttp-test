class UsersAPI:
    def users(self, id=None):
        return {
            'message': 'UserAPI {}'.format(id) if id is not None else 'UserAPI'
        }