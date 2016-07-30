#!/usr/bin/python


from bs4 import BeautifulSoup
import requests
from google import search
    
def start():
    college = college_choice()
    url = find(college)
    parse(url)

def college_choice():
    print "What college do you want to search for?"
    college = raw_input()
    return college

def find(college):
    for link in search(college + ' collegedata', stop=1):
        url = link
        break    
    return url

def parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    j = soup.find_all('table', {'class':'onecolumntable'})[1]
    admission = j.find_all('td')
    admit = admission[1].text
    ea = admission[2].text
    ed = admission[3].text
    k = soup.find_all('table', {'class':'onecolumntable'})[2]
    academics = k.find_all('td')
    gpa = academics[0].text
    satm = academics[1].text
    satr = academics[2].text
    satw = academics[3].text
    act = academics[4].text
    i = soup.find_all('table', {'class':'onecolumntable'})[3]
    finances = i.find_all('td')
    cost = finances[0].text
    need_met = finances[3].text
    p = soup.find_all('div', {'class':'cp_left'})
    college = p[0].text
    q = soup.find_all('table', {'class':'onecolumntable'})[0]
    gen_info = q.find_all('td')
    college_type = gen_info[1].text
    pop = gen_info[3].text
    print college
    print '\n'
    print 'About:\n Type: %s\n Undergraduate Population: %s\n' % (college_type, pop)
    print 'Admission:\n Rate: %s\t\n Early Action: %s\t\n Early Decision: %s\t\n' % (admit, ea, ed)
    print 'Academics:\n GPA: %s\n SAT Math: %s\n SAT Critical Reading: %s\n SAT Writing: %s\n ACT Composite: %s\n' % (gpa, satm, satr, satw, act)
    print 'Finances:\n Cost To Attend: %s\n Average Percent of Need Met: %s\n' % (cost, need_met)
    start()

start()
