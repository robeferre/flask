from sqlalchemy.sql import text
from lusers import db


class Users:

    @staticmethod
    def get_user(_user):
        if _user:
            _user = _user.replace(' ', '')

        results_obj = []
        sql = text('''
            SELECT U.CD_SENHA, U.NM_COMPLETO, U.NM_USUARIO, U.NM_E_MAIL, U.NM_CLASSE FROM TESCUSU0 U
                WHERE (U.NM_USUARIO = :user OR NM_E_MAIL = :user) AND
                U.CT_BLOQUEADO <> 'S' AND U.DH_EXCLUSAO IS NULL
                AND (U.DH_BLOQUEADO < sysdate() OR U.DH_BLOQUEADO IS NULL)
                AND ((U.TP_EXPIRACAO = 2 AND DATE_ADD(U.DH_ALTERACAO_SENHA, interval U.PZ_EXPIRACAO DAY) >  sysdate()) 
                OR U.TP_EXPIRACAO = 1)
                AND U.IC_SENHA_REDEF = 'N'
                ''')
        results = db.engine.execute(sql, user=_user)
        for row in results:
            obj = {
                'nome_usuario': str(row['NM_USUARIO']),
                'hash': str(row['CD_SENHA']),
                'nome_completo': row['NM_COMPLETO'],
                'email': row['NM_E_MAIL'],
                'tipo_usuario': row['NM_CLASSE'],
            }
            results_obj.append(obj)

        return results_obj
