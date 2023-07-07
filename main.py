from athena_logic import Athena
import athena_calendar as c


if __name__ == '__main__':
    # athena = Athena()
    cred = c.login()
    c.view_events(cred)
