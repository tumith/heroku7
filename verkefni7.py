import pymysql
from bottle import *

@get('/')
def index():
    return template('index')

@route('/donyskra', method='POST')
def nyr():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0412012660', passwd='mypassword', db='0412012660_verk7')
    cur = conn.cursor()

    cur.execute('SELECT count(*) FROM 0412012660_verk7.users where user=%s', (u))
    result = cur.fetchone()

    if result[0] == 0:
        cur.execute('INSERT INTO 0412012660_verk7.users Values(%s,%s,%s)', (u,p,n))
        conn.commit()
        cur.close()
        conn.close()
        return u, " Þú hvefur verið skráður <br> <a href='/'>Aftur Heim</a>"
    else:
        return u, " Þú getur ekki notað þetta nafn því það er eitthver annar að nota það <br> <a href='/#ny>Nyskran</a>'"

@route('/doinnskra', method='POST')
def doinn():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0412012660', passwd='mypassword', db='0412012660_verk7')
    cur = conn.cursor()

    cur.execute('SELECT count(*) FROM 0412012660_verk7.users where user=%s and pass=%s', (u,p))
    result = cur.fetchone()
    print(result)
    if result[0] == 1:

        cur.close()
        conn.close()
        return template('leyni',u=u)
    else:
        return template('ekkileyni')

@route('/members')
def members():
    conn = pymysql.connect(host="tsuts.tskoli.is",port=3306,user="0412012660",password="mypassword", db='0412012660_verk7')
    c = conn.cursor()
    c.execute("SELECT nafn FROM 0412012660_verk7.users")
    result = c.fetchall()
    c.close()
    output = template('members',rows = result)
    return output

try:
    run(host="0.0.0.0", port=os.environ.get('PORT'))
except:
    run(debug=True)
