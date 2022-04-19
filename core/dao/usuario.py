from psycopg2 import connect

class UsuarioDAO:

    @staticmethod
    def get_connection():
        return connect(host="localhost", database="postgres", user="postgres", password="dev")

    @staticmethod
    def teste():
        con = None
        value = None
        try:
            con = UsuarioDAO.get_connection()
            cur = con.cursor()
            cur.execute('Select version()')
            value = cur.fetchone()
            cur.close()
        except(Exception) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
        return value
