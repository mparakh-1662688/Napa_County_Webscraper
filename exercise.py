from lxml import html
from lxml.html import tostring
import sqlite3
from lxml import etree

# Only use a single URL at a time the three are only present as a sample
page_url = (

  # "http://ca.healthinspections.us/napa/search.cfm?start=1&1=1&sd=01/01/1970&ed=03/01/2017&kw1="
  # "&kw2=&kw3=&rel1=N.permitName&rel2=N.permitName&rel3=N.permitName&zc=&dtRng=YES&pre=similar"

  "http://ca.healthinspections.us/napa/search.cfm?start=11&1=1&sd=01/01/1970&ed=03/01/2017&kw1"
  "=&kw2=&kw3=&rel1=N.permitName&rel2=N.permitName&rel3=N.permitName&zc=&dtRng=YES&pre=similar"

  # "http://ca.healthinspections.us/napa/search.cfm?start=21&1=1&sd=01/01/1970&ed=03/01/2017"
  # "&kw1=&kw2=&kw3=&rel1=N.permitName&rel2=N.permitName&rel3=N.permitName&zc=&dtRng=YES&pre=similar"

)


# Helps create an empty 'Food' table with the required schema
def setup_db():
    conn = sqlite3.connect("exercise.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Food (Address varchar(255), State text, City varchar(100),"  
              "Zipcode INT, Inspection_date date, Grade text)")
    conn.commit()
    conn.close()

# This function will scrape the required information for the napa county website
# and would insert the relavant data into the database
def scrape():
    root = html.parse(page_url)
    main_address = root.xpath(".//div[@style='margin-bottom:10px;']/text()")
    inspection = root.xpath(".//div[@style='color:green;']/text()")
    date = root.xpath(".//a[@target='_blank']/text()")
    grade, street, city, state, area_zip = ([] for i in range(5))

    for x in range(1,20,2):
      st = inspection[x].strip()
      st = st[-1:]
      if (st == 'l'):
        st = "Fail"
      grade.append(st)

    for y in range(0,30,3):
      street.append(main_address[y].strip())

    for z in range(1,30,3):
      state_zip = main_address[z].strip()
      sz_array = state_zip.split(',')
      city.append(sz_array[0])
      state_initials = sz_array[1].split(' ')
      state.append(state_initials[1])
      area_zip.append(int(state_initials[2]))

    conn = sqlite3.connect("exercise.db")
    c = conn.cursor()

    for r in range(0,10):
      c.execute("INSERT INTO Food VALUES ('%s', '%s', '%s', '%d', '%s', '%s')"
                 % (street[r], state[r], city[r], area_zip[r], date[r], grade[r]))
    
    conn.commit()
    conn.close()  

    #print tostring(div)  # This is just for debug, you probably shouldn't actually use this

    # print date


def main():
    setup_db()
    scrape()


if __name__ == '__main__':
    main()
