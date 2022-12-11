import psycopg2
import time

hostname = 'localhost'
database = 'lab_1'
username = 'postgres'
pwd = '228psw1488'
port_id = 5432

conn = None
cur = None


try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
        )

    cur = conn.cursor()
except Exception as error:
    print(error)



def close_connection():
    if cur is not None:
        print('closing cursor')
        cur.close()
    if conn is not None:
        conn.close()



def employer_m(f, sf, upf):
    ins_scr = 'INSERT INTO employer (office_id, name, gender, date_of_birth) VALUES (%s, %s, %s, %s)'

       
    if f==1:
        ins_data = (int(input('enter office_id: ')), input('enter name: '), input('enter gender: '), input('enter date_of_birth: '))
        try:
            cur.execute(ins_scr, ins_data)
        except Exception as error:
            print(error)
        conn.commit()
            
    if f==2:
        if upf==1:
            del_scr = "DELETE FROM employer where name=%s;"
            del_scr1 = "DELETE FROM project_worker where employer_id=(SELECT id FROM employer where name=%s);"
            del_data = (input('enter name: '),)
            try:
                cur.execute(del_scr1, del_data)
                cur.execute(del_scr, del_data)
            except Exception as error:
                print(error)
            conn.commit()
        if upf==2:
            del_scr = "DELETE FROM employer where id=%s;"
            del_scr1 = "DELETE FROM project_worker where employer_id=%s;"
            del_data = (input('enter id: '),)
            try:
                cur.execute(del_scr1, del_data)
                cur.execute(del_scr, del_data)
            except Exception as error:
                print(error)
            conn.commit()
    if f==3:
        if sf==1:
            if upf==1:
                set_data = (input('enter name: '), input('by name: '))
                up_scr = "UPDATE employer SET name=%s where name=%s;"
            if upf==2:
                set_data = (input('enter name: '), input('by id: '))
                up_scr = "UPDATE employer SET name=%s where id=%s;"

        if sf==2:
            if upf==1:
                set_data = (input('enter gender: '), input('by name: '))
                up_scr = "UPDATE employer SET gender=%s where name=%s;"
            if upf==2:
                set_data = (input('enter gender: '), input('by id: '))
                up_scr = "UPDATE employer SET gender=%s where id=%s;"
            
        if sf==3:
            if upf==1:
                set_data = (input('enter date_of_birth: '), input('by name: '))
                up_scr = "UPDATE employer SET date_of_birth=%s where name=%s;"
            if upf==2:
                set_data = (input('enter date: '), input('by id: '))
                up_scr = "UPDATE employer SET date_of_birth=%s where id=%s;"
            
        if sf==4:
            if upf==1:
                set_data = (input('enter office_id: '), input('by name: '))
                up_scr = "UPDATE employer SET office_id=%s where name=%s;"
            if upf==2:
                set_data = (input('enter office_id: '), input('by id: '))
                up_scr = "UPDATE employer SET office_id=%s where id=%s;"

        try:
            cur.execute(up_scr, set_data)
        except Exception as error:
            print(error)
        conn.commit()

    if f==4:
        rand_scr = ("INSERT INTO employer (office_id, name, gender, date_of_birth) select office.id, chr((random()*25+65)::int)||chr((random()*25+65)::int)||chr((random()*25+65)::int)||chr((random()*25+65)::int)||chr((random()*25+65)::int), chr((random()*0+((random()*1+10)::int)*7)::int), date(timestamp '1940-01-01' + random() * (timestamp '2004-12-20' - timestamp '1940-01-01')) from office, generate_series(1,%s);")
        rand_data = (input('set limit: '),)
        try:
            cur.execute(rand_scr, rand_data)
        except Exception as error:
            print(error)
        conn.commit()

    if f==5:
        print('\nemployer table:')
        try:
            cur.execute("SELECT * from employer order by id")
            print('\nemp_id  |ofc_id |emp_name       |gender |date_of_birth  |')
            print('--------+-------+---------------+-------+---------------+')
            for flow in cur.fetchall():
                print(flow[0], '\t|', flow[1], '\t|', flow[2], '\t|', flow[3], '\t|', flow[4],)
            print('\n')
        except Exception as error:
            print(error)



def office_m(f, sf, upf):
    
    ins_scr = 'INSERT INTO office (company_id, placement, purpose) VALUES (%s, %s, %s)'
    
    if f==1:

        ins_data = (int(input('enter company_id: ')), input('enter placement: '), input('enter purpose: '))
        try:
            cur.execute(ins_scr, ins_data)
        except Exception as error:
            print(error)
        conn.commit()

    if f==2:
        if upf==1:
            del_scr = "DELETE FROM office where id=%s;"
            del_scr1 = "DELETE FROM employer where office_id=%s;"
            del_data = (input('enter id: '),)
            try:
                cur.execute(del_scr1, del_data)
                cur.execute(del_scr, del_data)
            except Exception as error:
                print(error)
            conn.commit()
    if f==3:
        if sf==1:
                
            if upf==1:
                set_data = (input('enter placment '), input('by placment: '))
                up_scr = "UPDATE office SET placement=%s where placment=%s;"
            if upf==2:
                set_data = (input('enter placment: '), input('by id: '))
                up_scr = "UPDATE office SET placement=%s where id=%s;"
            if upf==3:
                set_data = (input('enter placment: '), input('by purpose: '))
                up_scr = "UPDATE office SET placement=%s where purpose=%s;"

        if sf==2:

            if upf==1:
                set_data = (input('enter purpose '), input('by placment: '))
                up_scr = "UPDATE office SET purpose=%s where placment=%s;"
            if upf==2:
                set_data = (input('enter purpose: '), input('by id: '))
                up_scr = "UPDATE office SET purpose=%s where id=%s;"
            if upf==3:
                set_data = (input('enter purpose: '), input('by purpose: '))
                up_scr = "UPDATE office SET purpose=%s where purpose=%s;"
        
        try:
            cur.execute(up_scr, set_data)
        except Exception as error:
            print(error)
        conn.commit()
    
    if f==4:
        print('insertion of random data')
        rand_data = (int(input('set limit: ')),)
        rand_scr = "INSERT INTO office (company_id, placement, purpose) select 1, chr((random()*25+65)::int)||chr((random()*25+65)::int)||chr((random()*25+65)::int), chr((random()*25+65)::int)||chr((random()*25+65)::int)||chr((random()*25+65)::int) from generate_series(1,%s);"
        try:
            cur.execute(rand_scr, rand_data)
        except Exception as error:
            print(error)
        conn.commit()

    if f==5:
        print('\noffice table:')
        try:
            cur.execute("SELECT * from office;")
            print('\noffice_id       |company_id     |placement      |purpose                |')
            print('----------------+---------------+---------------+-----------------------+')
            for flow in cur.fetchall():
                print(flow[0], '\t\t|', flow[1], '\t\t|', flow[2], '\t|', flow[3],)
            print('\n')
        except Exception as error:
            print(error)


def project_worker_m(f, upf):
    if f==1:
        ins_scr = 'INSERT INTO project_worker (project_id, employer_id) VALUES (%s, %s)'
        ins_data = (int(input('enter project_id: ')), int(input('enter employer_id: ')))
        try:
            cur.execute(ins_scr, ins_data)
        except Exception as error:
            print(error)
        conn.commit()
    if f==2:
        if upf==1:
            del_scr = "DELETE FROM project_worker where project_id=%s;"
            del_data = (input('enter project_id: '),)
            try:
                cur.execute(del_scr, del_data)
            except Exception as error:
                print(error)
        if upf==2:
            del_scr = "DELETE FROM project_worker where employer_id = %s;"
            del_data = (input('enter employer_id: '),)
            try:
                cur.execute(del_scr, del_data)
            except Exception as error:
                print(error)
        if upf==3:
            del_scr = "DELETE FROM project_worker where project_id=%s and employer_id = %s;"
            del_data = (input('enter project_id: '), input('enter employer_id: '))
            try:
                cur.execute(del_scr, del_data)
            except Exception as error:
                print(error)
    
        conn.commit()
    if f==3:
        if upf==1:
            up_scr = "UPDATE project_worker SET project_id=%s where project_id=%s and employer_id=%s;"
            set_data = (input('SET project_id '), input('WHERE project_id '), input('AND employer_id '))

        if upf==2:
            up_scr = "UPDATE project_worker SET employer_id=%s where project_id=%s and employer_id=%s;;"
            set_data = (input('SET employer_id '), input('WHERE project_id '), input('AND employer_id '))
            
        try:
            cur.execute(up_scr, set_data)
        except Exception as error:
            print(error)
    if f==4:
        print('insertion of random data')
        hlp_scr1 = "delete from help_table;"
        hlp_scr2 = "insert into help_table (employer_id, project_id) select employer.id, project.id from employer, project;"
        ran_scr1 = "delete from project_worker;"
        ran_scr2 = "insert into project_worker (project_id, employer_id) select help_table.project_id, help_table.employer_id from help_table order by random() limit %s;"
        ran_data = (int(input('set limit: ')),)
        try:
            cur.execute(hlp_scr1)
            cur.execute(hlp_scr2)
            cur.execute(ran_scr1)
            cur.execute(ran_scr2, ran_data)
        except Exception as error:
            print(error)
        conn.commit()

    if f==5:
        print('\nproject_worker table:')
        try:
            cur.execute("SELECT * from project_worker;")
            print('\nproject_id      |employer_id    |')
            print('----------------+---------------+')
            for flow in cur.fetchall():
                print(flow[0], '\t\t|', flow[1],)
            print('\n')
        except Exception as error:
            print(error)

def project_m(f, upf):
    
    if f==1:
        ins_scr = 'INSERT INTO project (name, creation_date) VALUES (%s, %s)'
        ins_data = (input('enter name: '), input('enter creation_date: '))
        try:
            cur.execute(ins_scr, ins_data)
        except Exception as error:
            print(error)
        conn.commit()
    if f==2:
        del_scr = "DELETE FROM project where id = %s;"
        del_scr1 = "DELETE FROM project_worker where project_id = %s;"
        del_data = (input('enter id: '),)
        try:
            cur.execute(del_scr1, del_data)
            cur.execute(del_scr, del_data)
        except Exception as error:
            print(error)
        conn.commit()
    if f==3:
        if upf==1:
            up_scr = "UPDATE project SET id=%s where id=%s;"
            set_data = (input('SET id '), input('WHERE id '), )
        if upf==2:
            up_scr = "UPDATE project SET name=%s where id=%s;"
            set_data = (input('SET name '), input('WHERE id '), )
        if upf==3:
            up_scr = "UPDATE project SET creation_date=%s where id=%s;"
            set_data = (input('SET creation_date '), input('WHERE id '), )
        try:
            cur.execute(up_scr, set_data)
        except Exception as error:
            print(error)
        conn.commit()
    if f==4:
        print('isertion of random data\n')
        rand_data = (int(input('set limit: ')), )
        rand_scr = "INSERT INTO project (name, creation_date) SELECT chr((random()*25+65)::int)||chr((random()*25+65)::int)||chr((random()*25+65)::int), date(timestamp '2001-01-01' + random() * (timestamp '2004-12-20' - timestamp '2001-01-01')) from generate_series(1,%s);"
        try:
            cur.execute(rand_scr, rand_data)
        except Exception as error:
            print(error)
        conn.commit()
    if f==5:
        print('\nproject table:')
        try:
            cur.execute("SELECT * from project;")
            print('\nid      |name                   |creation_date  |')
            print('--------+-----------------------+---------------+')
            for flow in cur.fetchall():
                print(flow[0], '\t|', flow[1], '\t\t|', flow[2],)
            print('\n')
        except Exception as error:
            print(error)


def joins_m(f, by_f):
    if f==1:
        if by_f==1:
            join_data = (input('LIKE: '), )
            try:
                begin_t = time.perf_counter()
                cur.execute("SELECT * from employer as em INNER JOIN project_worker as pw on em.id=pw.employer_id INNER JOIN project as prj on pw.project_id=prj.id where em.name LIKE %s;", join_data)
                end_t = time.perf_counter()
                print('\nemp_id  |office_id      |emp_name       |gender |date_of_birth  |project_id     |employer_id    |prj_id |prj_name       |creation_date  |')
                print('--------+---------------+---------------+-------+---------------+---------------+---------------+-------+---------------+---------------+')
                for flow in cur.fetchall():
                    print(flow[0], '\t|', flow[1], '\t\t|', flow[2], '\t|', flow[3], '\t|', flow[4], '\t|', flow[5], '\t\t|', flow[6], '\t\t|', flow[7], '\t|', flow[8], '\t|', flow[9], '\t|',)
                print('\n')
                print('QUERY TIME: ',end_t-begin_t, "milliseconds")
            except Exception as error:
                print(error)
        if by_f==2:
            join_data = (input('LIKE: '), input('prj_id: '))
            try:
                begin_t = time.perf_counter()
                cur.execute("SELECT * from employer as em INNER JOIN project_worker as pw on em.id=pw.employer_id INNER JOIN project as prj on pw.project_id=prj.id where em.name LIKE %s and prj.id=%s;", join_data)
                end_t = time.perf_counter()
                print('\nemp_id  |office_id      |emp_name       |gender |date_of_birth  |project_id     |employer_id    |prj_id |prj_name       |creation_date  |')
                print('--------+---------------+---------------+-------+---------------+---------------+---------------+-------+---------------+---------------+')
                for flow in cur.fetchall():
                    print(flow[0], '\t|', flow[1], '\t\t|', flow[2], '\t|', flow[3], '\t|', flow[4], '\t|', flow[5], '\t\t|', flow[6], '\t\t|', flow[7], '\t|', flow[8], '\t|', flow[9], '\t|',)
                print('\n')
                print('QUERY TIME: ',end_t-begin_t, "milliseconds")
            except Exception as error:
                print(error)
        if by_f==3:
            join_data = (input('employer gender: '), input('prj_creation_date(left): '), input('prj_creation_date(right): '))
            try:
                begin_t = time.perf_counter()
                cur.execute("SELECT * from employer as em INNER JOIN project_worker as pw on em.id=pw.employer_id INNER JOIN project as prj on pw.project_id=prj.id where em.gender=%s and prj.creation_date between %s and %s;", join_data)
                end_t = time.perf_counter()
                print('\nemp_id  |office_id      |emp_name       |gender |date_of_birth  |project_id     |employer_id    |prj_id |prj_name       |creation_date  |')
                print('--------+---------------+---------------+-------+---------------+---------------+---------------+-------+---------------+---------------+')
                for flow in cur.fetchall():
                    print(flow[0], '\t|', flow[1], '\t\t|', flow[2], '\t|', flow[3], '\t|', flow[4], '\t|', flow[5], '\t\t|', flow[6], '\t\t|', flow[7], '\t|', flow[8], '\t|', flow[9], '\t|',)
                print('\n')
                print('QUERY TIME: ',end_t-begin_t, "milliseconds")
            except Exception as error:
                print(error)
    
    if f==2:
        if by_f==1:
            join_data = (input('employer name: '), int(input('office_id: ')))
            try:
                begin_t = time.perf_counter()
                cur.execute("SELECT * from employer as em INNER JOIN office as ofc on ofc.id=em.office_id where em.name LIKE %s and office_id=%s;", join_data)
                end_t = time.perf_counter()
                print('\nemp_id  |ofc_id |emp_name       |gender |date_of_birth  |office_id      |company_id     |placement      |purpose                |')
                print('--------+-------+---------------+-------+---------------+---------------+---------------+---------------+-----------------------+')
                for flow in cur.fetchall():
                    print(flow[0], '\t|', flow[1], '\t|', flow[2], '\t|', flow[3], '\t|', flow[4], '\t|', flow[5], '\t\t|', flow[6], '\t\t|', flow[7], '\t|', flow[8], '\t|',)
                print('\n')
                print('QUERY TIME: ',end_t-begin_t, "milliseconds")
            except Exception as error:
                print(error)
        if by_f==2:
            join_data = (input('employer gender: '), input('employer date_of_birth(left): '), input('employer date_of_birth(right): '))
            try:
                begin_t = time.perf_counter()
                cur.execute("SELECT * from employer as em INNER JOIN office as ofc on ofc.id=em.office_id where em.gender=%s and em.date_of_birth between %s and %s;", join_data)
                end_t = time.perf_counter()
                print('\nemp_id  |ofc_id |emp_name       |gender |date_of_birth  |office_id      |company_id     |placement      |purpose                |')
                print('--------+-------+---------------+-------+---------------+---------------+---------------+---------------+-----------------------+')
                for flow in cur.fetchall():
                    print(flow[0], '\t|', flow[1], '\t|', flow[2], '\t|', flow[3], '\t|', flow[4], '\t|', flow[5], '\t\t|', flow[6], '\t\t|', flow[7], '\t|', flow[8], '\t|',)
                print('\n')
                print('QUERY TIME: ',end_t-begin_t, "milliseconds")
            except Exception as error:
                print(error)


