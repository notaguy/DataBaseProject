from time import strftime

from flask import Flask, render_template, jsonify, request, redirect
import cx_Oracle
from datetime import datetime
import re

app = Flask(__name__)
with open(app.root_path + '\config.cfg', 'r') as f:
    app.config['ORACLE_URI'] = f.readline()

con = cx_Oracle.connect("bd125", "bd125", "bd-dc.cs.tuiasi.ro:1539/orcl")


# pacient begin code
@app.route('/')
@app.route('/pacient') #numele fisierului in html
def pac():
    pacient = []

    cur = con.cursor()
    cur.execute('select * from pacient order by pacient_id')
    for result in cur:
        pac = {}
        pac['pacient_id'] = result[6]
        pac['nume'] = result[0]
        pac['prenume'] = result[1]
        pac['varsta'] = result[2]
        pac['gen'] = result[3]
        pac['telefon'] = result[4]
        pac['email'] = result[5]
        pacient.append(pac)
    cur.close()
    return render_template('pacient.html', pacient=pacient)

# -----------------
@app.route('/nouPacient', methods=['GET', 'POST'])
def add_pac():
    error = None
    if request.method == 'POST':
        emp = 0
        cur = con.cursor()
        cur.execute('select max(pacient_id) from pacient')
        for result in cur:
            emp = result[0]
        cur.close()
        emp += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(emp) + "'")
        values.append("'" + request.form['nume'] + "'")
        values.append("'" + request.form['prenume'] + "'")
        values.append("'" + request.form['varsta'] + "'")
        values.append("'" + request.form['gen'] + "'")
        values.append("'" + request.form['telefon'] + "'")
        values.append("'" + request.form['email'] + "'")

        fields = ['pacient_id', 'nume', 'prenume', 'varsta', 'gen', 'telefon', 'email']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('pacient', ', '.join(fields), ', '.join(values))

        cur.execute(query)
        cur.execute('commit')
        return redirect('/pacient')
    else:
        job = []
        cur = con.cursor()
        cur.execute('select job_id from Jobs')
        for result in cur:
            job.append(result[0])
        cur.close()

        return render_template('nouPacient.html', Jobs=job)

@app.route('/editPacient', methods=['POST'])
def edit_emp():
    emp = 0
    cur = con.cursor()
    nume = "'" + request.form['nume'] + "'"

    cur.execute('select pacient_id from pacient where nume=' + nume)
    for result in cur:
        emp = result[0]
    cur.close()
    prenume = "'" + request.form['prenume'] + "'"
    varsta = request.form['varsta']
    gen = "'" + request.form['gen'] + "'"
    telefon = "'" + request.form['telefon'] + "'"
    email = "'" + request.form['email'] + "'"

    cur = con.cursor()
    query = "UPDATE pacient SET nume=%s, prenume=%s, varsta=%s, gen=%s, telefon=%s, email=%s where pacient_id=%s" % (
    nume, prenume, varsta, gen, telefon, email, emp)

    cur.execute(query)
    cur.execute('commit')
    return redirect('/pacient')


@app.route('/getPacient', methods=['POST'])
def get_pac():
    emp = request.form['pacient_id']
    cur = con.cursor()
    cur.execute('select * from pacient where pacient_id=' + emp)
    emps = cur.fetchone()
    nume = emps[0]
    prenume = emps[1]
    varsta = emps[2]
    gen = emps[3]
    telefon = emps[4]
    email = emps[5]
    cur.close()

    return render_template('editPacient.html', nume=nume, prenume=prenume, varsta=varsta, gen=gen, telefon=telefon, email=email)

@app.route('/delPacient', methods=['POST'])
def del_pac():
    c = "'" + request.form['pacient_id'] + "'"
    cur = con.cursor()
    cur.execute('delete from pacient where pacient_id=' + c)
    cur.execute('commit')
    return redirect('/pacient')

# pacient end code
# ------------------------------------------#
# cmd start code
@app.route('/cmd')
def cmd():
    cmd = []

    cur = con.cursor()
    cur.execute('select * from cmd order by cmd_id')
    for result in cur:
        cmdv = {}
        cmdv['cmd_id'] = result[1]
        cmdv['descriere'] = result[0]
        cmd.append(cmdv)
    cur.close()
    return render_template('cmd.html', cmd=cmd)


@app.route('/addCMD', methods=['POST'])
def ad_cmd():
    error = None
    if request.method == 'POST':
        emp = 0
        cur = con.cursor()
        cur.execute('select max(cmd_id) from cmd')
        for result in cur:
            emp = result[0]
        cur.close()
        emp += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(emp) + "'")
        values.append("'" + request.form['descriere'] + "'")
        fields = ['cmd_id', 'descriere']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            'cmd',
            ', '.join(fields),
            ', '.join(values)
        )

        cur.execute(query)
        cur.execute('commit')
        return redirect('/cmd')


@app.route('/delCMD', methods=['POST'])
def del_cmd():
    c = "'" + request.form['cmd_id'] + "'"
    cur = con.cursor()
    cur.execute('delete from cmd where cmd_id=' + c)
    cur.execute('commit')
    return redirect('/cmd')


# cmd end code
# ------------------------------------------#
# specializari start code
@app.route('/specializari')
def spec():
    specializari = []

    cur = con.cursor()
    cur.execute('select * from specializari order by specializare_id')
    for result in cur:
        spec = {}
        spec['specializare_id'] = result[1]
        spec['denumire'] = result[0]
        specializari.append(spec)
    cur.close()
    return render_template('specializari.html', specializari=specializari)


@app.route('/addSpec', methods=['POST'])
def ad_spec():
    error = None
    if request.method == 'POST':
        emp = 0
        cur = con.cursor()
        cur.execute('select max(specializare_id) from specializari')
        for result in cur:
            emp = result[0]
        cur.close()
        emp += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(emp) + "'")
        values.append("'" + request.form['denumire'] + "'")
        fields = ['specializare_id', 'denumire']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            'specializari',
            ', '.join(fields),
            ', '.join(values)
        )
        cur.execute(query)
        cur.execute('commit')
        return redirect('/specializari')

@app.route('/delSpec', methods=['POST'])
def del_spec():
    s = "'" + request.form['specializare_id'] + "'"
    cur = con.cursor()
    cur.execute('delete from specializari where specializare_id=' + s)
    cur.execute('commit')
    return redirect('/specializari')


# specializari end code
# -----------------------------------------#
# istoric start code
@app.route('/istoric_initial')
def istoric():
    istoric = []

    cur = con.cursor()
    cur.execute('select * from istoric_initial order by pacient_pacient_id')
    for result in cur:
        isto = {}
        isto['pacient_pacient_id'] = result[3]
        isto['boli_anterioare'] = result[0]
        isto['alergii'] = result[1]
        isto['tratament_curent'] = result[2]
        istoric.append(isto)
    cur.close()

    com = []
    cur = con.cursor()
    cur.execute('select pacient_id from pacient')
    # import pdb;pdb.set_trace()
    for result in cur:
        com.append(result[0])
    cur.close()

    return render_template('istoric_initial.html', istoric=istoric, istoric_initial=com)


@app.route('/addIstoric', methods=['POST'])
def ad_istoric():
    error = None
    if request.method == 'POST':
        cur = con.cursor()
        values = []
        values.append("'" + request.form['pacient_pacient_id'] + "'")
        values.append("'" + request.form['boli_anterioare'] + "'")
        values.append("'" + request.form['alergii'] + "'")
        values.append("'" + request.form['tratament_curent'] + "'")
        fields = ['pacient_pacient_id', 'boli_anterioare', 'alergii', 'tratament_curent']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            'istoric_initial',
            ', '.join(fields),
            ', '.join(values)
        )

        cur.execute(query)
        cur.execute('commit')
        return redirect('/istoric_initial')


@app.route('/delIstoric', methods=['POST'])
def del_istoric():
    c = "'" + request.form['pacient_pacient_id'] + "'"
    cur = con.cursor()
    cur.execute('delete from istoric_initial where pacient_pacient_id=' + c)
    cur.execute('commit')
    return redirect('/istoric_initial')


# istoric end code
# -----------------------------------------#
# medic start code
@app.route('/medic')
def med():
    medicc = []

    cur = con.cursor()
    cur.execute('select * from medic order by medic_id')
    for result in cur:
        med = {}
        med['medic_id'] = result[2]
        med['nume'] = result[0]
        med['prenume'] = result[1]
        med['specializari_specializare_id'] = result[3]
        medicc.append(med)
    cur.close()

    com = []
    cur = con.cursor()
    cur.execute('select specializare_id from specializari')
    # import pdb;pdb.set_trace()
    for result in cur:
        com.append(result[0])
    cur.close()

    return render_template('medic.html', medicc=medicc, medic=com)


@app.route('/addMedic', methods=['POST'])
def ad_medic():
    error = None
    if request.method == 'POST':
        m = 0
        cur = con.cursor()
        cur.execute('select max(medic_id) from medic')
        for result in cur:
            m = result[0]
        cur.close()
        m += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(m) + "'")
        values.append("'" + request.form['nume'] + "'")
        values.append("'" + request.form['prenume'] + "'")
        values.append("'" + request.form['specializari_specializare_id'] + "'")
        fields = ['medic_id', 'nume', 'prenume', 'specializari_specializare_id']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            'medic',
            ', '.join(fields),
            ', '.join(values)
        )
        cur.execute(query)
        cur.execute('commit')
        return redirect('/medic')

@app.route('/delMedic', methods=['POST'])
def del_medic():
    c = "'" + request.form['medic_id'] + "'"
    cur = con.cursor()
    cur.execute('delete from medic where medic_id=' + c)
    cur.execute('commit')
    return redirect('/medic')


# medic end code
# -----------------------------------------#
#programare begin code
@app.route('/programare') #numele fisierului in html
def prog():
    program = []

    cur = con.cursor()
    cur.execute('select * from programare order by programare_id')
    for result in cur:
        prog = {}
        prog ['programare_id'] = result[4]
        prog ['data_ora'] = result[0]
        prog ['etaj'] = result[1]
        prog ['sala'] = result[2]
        prog['serviciu'] = result[3]
        prog['pacient_pacient_id'] = result[5]
        prog['medic_medic_id'] = result[6]
        program.append(prog)
    cur.close()

    com = []
    cur = con.cursor()
    cur.execute('select pacient_id from pacient')
    # import pdb;pdb.set_trace()
    for result in cur:
        com.append(result[0])
    cur.close()

    comm = []
    cur = con.cursor()
    cur.execute('select medic_id from medic')
    # import pdb;pdb.set_trace()
    for result in cur:
        comm.append(result[0])
    cur.close()

    return render_template('programare.html', program=program, programare=com)

# -----------------
@app.route('/addProgramare', methods=['GET', 'POST'])
def add_prog():
    error = None
    if request.method == 'POST':
        emp = 0
        cur = con.cursor()
        cur.execute('select max(programare_id) from programare')
        for result in cur:
            emp = result[0]
        cur.close()
        emp += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(emp) + "'")
        values.append("to_timestamp(" + "substr(" + "'" + request.form['data_ora'] + "', 1, 10)" + "||" + "substr(" + "'" +request.form['data_ora'] + "', 12, 8)" + ", " + "'YYYY-MM-DD HH24:MI:SS')")
        values.append("'" + request.form['etaj'] + "'")
        values.append("'" + request.form['sala'] + "'")
        values.append("'" + request.form['serviciu'] + "'")
        values.append("'" + request.form['pacient_pacient_id'] + "'")
        values.append("'" + request.form['medic_medic_id'] + "'")

        fields = ['programare_id', 'data_ora', 'etaj', 'sala', 'serviciu', 'pacient_pacient_id', 'medic_medic_id']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % ('programare', ', '.join(fields), ', '.join(values))
        print(query)
        cur.execute(query)
        cur.execute('commit')
        return redirect('/programare')

@app.route('/editProgramare', methods=['POST'])
def edit_prog():
    emp = 0
    cur = con.cursor()
    pacient_pacient_id = "'" + request.form['pacient_pacient_id'] + "'"

    cur.execute('select programare_id from programare where pacient_pacient_id=' + pacient_pacient_id)
    for result in cur:
        emp = result[0]
    cur.close()
    data_ora = "to_timestamp(" + "substr(" + "'" + request.form['data_ora'] + "', 1, 10)" + "||" + "substr(" + "'" +request.form['data_ora'] + "', 12, 8)" + ", " + "'YYYY-MM-DD HH24:MI:SS')"
    etaj = request.form['etaj']
    sala = request.form['sala']
    serviciu = "'" + request.form['serviciu'] + "'"
    medic_medic_id = request.form['medic_medic_id']

    cur = con.cursor()
    query = "UPDATE programare SET data_ora=%s, etaj=%s, sala=%s, serviciu=%s, medic_medic_id=%s where programare_id=%s" % (
    data_ora, etaj, sala, serviciu, medic_medic_id, emp)
    print(query)
    cur.execute(query)
    cur.execute('commit')
    return redirect('/programare')


@app.route('/getProgramare', methods=['POST'])
def get_prog():
    emp = request.form['programare_id']
    cur = con.cursor()
    cur.execute('select * from programare where programare_id=' + emp)

    emps = cur.fetchone()
    data_ora = emps[0]
    etaj = emps[1]
    sala = emps[2]
    serviciu = emps[3]
    medic_medic_id = emps[6]
    pacient_pacient_id = emps[5]

    cur.close()

    return render_template('editProgramare.html', data_ora=data_ora, etaj=etaj, sala=sala, serviciu=serviciu, medic_medic_id=medic_medic_id, pacient_pacient_id=pacient_pacient_id)

@app.route('/delProgramare', methods=['POST'])
def del_prog():
    c = "'" + request.form['programare_id'] + "'"
    cur = con.cursor()
    cur.execute('delete from programare where programare_id=' + c)
    cur.execute('commit')
    return redirect('/programare')

# programare end code
# -----------------------------------------#
# tratament start code
@app.route('/tratament')
def tratament():
    tratam = []

    cur = con.cursor()
    cur.execute('select * from tratament order by diagnostic_diagnostic_id')
    for result in cur:
        tra = {}
        tra['diagnostic_diagnostic_id'] = result[4]
        tra['nume_pastila'] = result[0]
        tra['cantitate'] = result[1]
        tra['interval_administrare'] = result[2]
        tra['durata_tratament'] = result[3]
        tratam.append(tra)
    cur.close()

    com = []
    cur = con.cursor()
    cur.execute('select diagnostic_id from diagnostic')
    # import pdb;pdb.set_trace()
    for result in cur:
        com.append(result[0])
    cur.close()

    return render_template('tratament.html', tratam=tratam, tratament=com)


@app.route('/addTratament', methods=['POST'])
def ad_tratament():
    error = None
    if request.method == 'POST':
        cur = con.cursor()
        values = []
        values.append("'" + request.form['diagnostic_diagnostic_id'] + "'")
        values.append("'" + request.form['nume_pastila'] + "'")
        values.append("'" + request.form['cantitate'] + "'")
        values.append("'" + request.form['interval_administrare'] + "'")
        values.append("'" + request.form['durata_tratament'] + "'")
        fields = ['diagnostic_diagnostic_id', 'nume_pastila', 'cantitate', 'interval_administrare', 'durata_tratament']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            'tratament',
            ', '.join(fields),
            ', '.join(values)
        )

        cur.execute(query)
        cur.execute('commit')
        return redirect('/tratament')


@app.route('/delTratament', methods=['POST'])
def del_tratament():
    c = "'" + request.form['diagnostic_diagnostic_id'] + "'"
    cur = con.cursor()
    cur.execute('delete from tratament where diagnostic_diagnostic_id=' + c)
    cur.execute('commit')
    return redirect('/tratament')


# tratament end code
# -----------------------------------------#
# diagnostic start code
@app.route('/diagnostic')
def diag():
    diagno = []

    cur = con.cursor()
    cur.execute('select * from diagnostic order by diagnostic_id')
    for result in cur:
        dig = {}
        dig['diagnostic_id'] = result[3]
        dig['denumire'] = result[0]
        dig['detalii'] = result[1]
        dig['simptome'] = result[2]
        dig['programare_programare_id'] = result[4]
        dig['cmd_cmd_id'] = result[5]
        diagno.append(dig)
    cur.close()

    com = []
    cur = con.cursor()
    cur.execute('select programare_id from programare')
    # import pdb;pdb.set_trace()
    for result in cur:
        com.append(result[0])
    cur.close()

    comm = []
    cur = con.cursor()
    cur.execute('select cmd_id from cmd')
    # import pdb;pdb.set_trace()
    for result in cur:
        comm.append(result[0])
    cur.close()

    return render_template('diagnostic.html', diagno=diagno, diagnostic=com)


@app.route('/addDiagnostic', methods=['POST'])
def ad_diagnostic():
    error = None
    if request.method == 'POST':
        m = 0
        cur = con.cursor()
        cur.execute('select max(diagnostic_id) from diagnostic')
        for result in cur:
            m = result[0]
        cur.close()
        m += 1
        cur = con.cursor()
        values = []
        values.append("'" + str(m) + "'")
        values.append("'" + request.form['denumire'] + "'")
        values.append("'" + request.form['detalii'] + "'")
        values.append("'" + request.form['simptome'] + "'")
        values.append("'" + request.form['programare_programare_id'] + "'")
        values.append("'" + request.form['cmd_cmd_id'] + "'")
        fields = ['diagnostic_id', 'denumire', 'detalii', 'simptome', 'programare_programare_id', 'cmd_cmd_id']
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            'diagnostic',
            ', '.join(fields),
            ', '.join(values)
        )
        cur.execute(query)
        cur.execute('commit')
        return redirect('/diagnostic')

@app.route('/editDiagnostic', methods=['POST'])
def edit_dig():
    emp = 0
    cur = con.cursor()
    denumire = "'" + request.form['denumire'] + "'"

    cur.execute('select diagnostic_id from diagnostic where denumire=' + denumire)
    for result in cur:
        emp = result[0]
    cur.close()
    detalii = "'" + request.form['detalii'] + "'"
    simptome = "'" + request.form['simptome']+ "'"
    programare_programare_id = request.form['programare_programare_id']
    cmd_cmd_id = request.form['cmd_cmd_id']

    cur = con.cursor()
    query = "UPDATE diagnostic SET denumire=%s, detalii=%s, simptome=%s, programare_programare_id=%s, cmd_cmd_id=%s where diagnostic_id=%s" % (
    denumire, detalii, simptome, programare_programare_id, cmd_cmd_id, emp)

    cur.execute(query)
    cur.execute('commit')
    return redirect('/diagnostic')


@app.route('/getDiagnostic', methods=['POST'])
def get_dig():
    emp = request.form['diagnostic_id']
    cur = con.cursor()
    cur.execute('select * from diagnostic where diagnostic_id=' + emp)

    emps = cur.fetchone()
    denumire = emps[0]
    detalii = emps[1]
    simptome = emps[2]
    programare_programare_id = emps[3]
    cmd_cmd_id = emps[4]
    cur.close()

    return render_template('editDiagnostic.html', denumire=denumire, detalii=detalii, simptome=simptome, programare_programare_id=programare_programare_id, cmd_cmd_id=cmd_cmd_id)

@app.route('/delDiagnostic', methods=['POST'])
def del_diag():
    s = "'" + request.form['diagnostic_id'] + "'"
    cur = con.cursor()
    cur.execute('delete from diagnostic where diagnostic_id=' + s)
    cur.execute('commit')
    return redirect('/diagnostic')
# diagnostic end code
# -----------------------------------------#

# main
if __name__ == '__main__':
    app.run(debug=True)
    con.close()
