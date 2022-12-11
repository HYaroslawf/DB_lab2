import psycopg2
import time
from model import *

hostname = 'localhost'
database = 'lab_1'
username = 'user'
pwd = 'password'
port_id = 5432



def employer():
    f = -1
    ins_scr = 'INSERT INTO employer (office_id, name, gender, date_of_birth) VALUES (%s, %s, %s, %s)'

    while f != 0:
        print('employer table:\n1 - insert\n2 - delete\n3 - update\n4 - generate random\n5 - show table\n0 - exit\n')
        f = int(input('enter your choice: '))
            
        if f==1:
            employer_m(1, 0, 0)
                
        if f==2:
            print('DELETE:\n1 - by name\n2 - by id\n')
            upf = int(input('enter your choice: '))
            if upf==1:
                employer_m(2, 0, 1)
            if upf==2:
                employer_m(2, 0, 2)
        if f==3:
            print('SET:\n1 - name\n2 - gender\n3 - date_of_birth\n4 - office_id')
            sf = int(input('enter your choice: '))
            if sf==1:
                    
                print('UPDATE:\n1 - by name\n2 - by id\n')
                upf = int(input('enter your choice: '))
                if upf==1:
                    employer_m(3, 1, 1)
                if upf==2:
                    employer_m(3, 1, 2)

            if sf==2:
                print('UPDATE:\n1 - by name\n2 - by id\n')
                upf = int(input('enter your choice: '))
                if upf==1:
                    employer_m(3, 2, 1)
                if upf==2:
                    employer_m(3, 2, 2)
                
            if sf==3:
                print('UPDATE:\n1 - by name\n2 - by id\n')
                upf = int(input('enter your choice: '))
                if upf==1:
                    employer_m(3, 3, 1)
                if upf==2:
                    employer_m(3, 3, 2)
                
            if sf==4:
                print('UPDATE:\n1 - by name\n2 - by id\n')
                upf = int(input('enter your choice: '))
                if upf==1:
                    employer_m(3, 4, 1)
                if upf==2:
                    employer_m(3, 4, 2)

        if f==4:
            employer_m(4, 0, 0)

        if f==5:
            employer_m(5, 0, 0)


    
    

def office():
    f = -1
    while f!=0:
        ins_scr = 'INSERT INTO office (company_id, placement, purpose) VALUES (%s, %s, %s)'
        print('office table:\n1 - insert\n2 - delete\n3 - update\n4 - generate random\n5 - show table\n0 - exit\n')
        f = int(input('enter your choice: '))
        if f==1:
            office_m(1, 0, 0)
        if f==2:
            print('DELETE:\n1 - by id\n0 - exit')
            upf = int(input('enter your choice: '))
            if upf==1:
                office_m(2, 0, 1)
        if f==3:
            print('SET:\n1 - placment\n2 - purpose\n')
            sf = int(input('enter your choice: '))
            if sf==1:
                    
                print('UPDATE:\n1 - by placment\n2 - by id\n3 - purpose')
                upf = int(input('enter your choice: '))
                if upf==1:
                    office_m(3, 1, 1)
                if upf==2:
                    office_m(3, 1, 2)
                if upf==3:
                    office_m(3, 1, 3)

            if sf==2:
                print('UPDATE:\n1 - by placment\n2 - by id\n3 - purpose')
                upf = int(input('enter your choice: '))
                if upf==1:
                    office_m(3, 2, 1)
                if upf==2:
                    office_m(3, 2, 2)
                if upf==3:
                    office_m(3, 2, 3)
            
        
        if f==4:
            office_m(4, 0, 0)

        if f==5:
            office_m(5, 0, 0)
            

def project():
    f = -1
    while f!=0:
        print('project table:\n1 - insert\n2 - delete\n3 - update\n4 - generate random\n5 - show table\n0 - exit\n')
        f = int(input('enter your choice: '))
        if f==1:
            project_m(1, 0)
        if f==2:
            project_m(2, 0)
        if f==3:
            print('UPDATE:\n1 - id\n2 - name\n3 - creation_date\n0 - exit\n')
            upf = int(input('enter your choice: '))
            if upf==1:
                project_m(3, 1)
            if upf==2:
                project_m(3, 2)
            if upf==3:
                project_m(3, 3)
        if f==4:
            project_m(4, 0)
        if f==5:
            project_m(5, 0)

def project_worker():
    f = -1
    while f!=0:
        print('\nproject_worker table: \n1 - insert\n2 - delete\n3 - update\n4 - generate random\n5 - show table\n0 - exit\n')
        f = int(input('enter your choice: '))
        if f==1:
            project_worker_m(1, 0)
        if f==2:
            print('DELETE:\n1 - by project_id\n2 - by employer_id\n3 - by both_id\n0 - exit')
            upf = int(input('enter your choice: '))
            if upf==3:
                project_worker_m(2, 1)
            if upf==2:
                project_worker_m(2, 2)
            if upf==3:
                project_worker_m(2, 3)
        
            conn.commit()
        if f==3:
            print('SET:\n1 - project_id\n2 - employer_id\n')
            upf = int(input('enter your choice: '))
            if upf==1:
                project_worker_m(3, 1)

            if upf==2:
                project_worker_m(3, 2)
                
        if f==4:
            project_worker_m(4, 0)

        if f==5:
            project_worker_m(5, 0)


    
def joins():
    f=-1
    while f!=0:
        print('JOIN:\n1 - employer, project_worker, project\n2 - employer, office\n0 - exit')
        f = int(input('your choice: '))
        if f==1:
            print('\nBY:\n1 - employer name\n2 - employer name AND project_id\n3 - employer gender AND project creation_date')
            by_f = int(input('your choice: '))
            if by_f==1:
                joins_m(1,1)
            if by_f==2:
                joins_m(1,2)
            if by_f==3:
                joins_m(1,3)
        
        if f==2:
            print('\nBY:\n1 - employer name and office_id\n2 - employer gender and date_of_birth')
            by_f = int(input('your choice: '))
            if by_f==1:
                joins_m(2,1)
            if by_f==2:
                joins_m(2,2)
        



flag = -1

while flag!=0:
    print('\nMAIN MENU:\n1 - employer\n2 - office\n3 - project_worker\n4 - project\n5 - joins\n0 - exit\n')
    flag = int(input('enter your choice: '))
    if flag == 1:
        employer()
    if flag == 2:
        office()
    if flag == 3:
        project_worker()
    if flag == 4:
        project()
    if flag == 5:
        joins()

    

print("PROGRAM ENDED")


