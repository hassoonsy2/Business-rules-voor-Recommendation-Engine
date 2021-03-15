import psycopg2
from psycopg2 import Error


def connect():
    """This function is the connection with the postgres db"""

    connection = psycopg2.connect(host='localhost', database='huwebshop', user='postgres', password='Xplod_555')
    return connection

def disconnect():
    """This function disconnects the program with the postgres db"""
    con = connect()
    return con.close()

def sql_execute(sql,value):
    """This function executes a query on the Postgres db"""
    c = connect()
    cur = c.cursor()
    cur.execute(sql,value)


def sql_select(sql):
    """This function select values from the tables on the Postgres db"""
    c = connect()
    cur = c.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    return results


def sql_query(sql):
    """This function executes a query on the Postgres db """
    c = connect()
    cur = c.cursor()
    cur.execute(sql)

def commit():
   """This function will cpmmit  a query on the Postgres db """
   c = connect()
   c.commit()




#                                                                                                     >> { Content-Based Filtering } <<<


def select_most_sold_products():
    """ This function will Select & count every product from Tabel Orders on the Postgres db """

    try:
        return sql_select("""SELECT orders.prodid, products.name,
                       COUNT(*)
                       FROM orders
                       INNER JOIN products ON Orders.prodid = products.id
                       GROUP BY prodid ,products.name 
                       ORDER BY COUNT(*) DESC ; """)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



            

def best_seller():
    """This function will Create Tabel Best seller on the Postgres db  """
    try:
         sql_query("DROP TABLE IF EXISTS Best_seller CASCADE")

         sql_query("""CREATE TABLE Best_seller                                
                            (prodid VARCHAR PRIMARY KEY,                        
                            name VARCHAR,                                       
                            Counter INTEGER ,                                   
                            FOREIGN KEY (prodid) REFERENCES products(id));""")


         results = select_most_sold_products()

        #Right , now we can insert the result into the Tabel

         for row  in results:
             prodid = row[0]
             name = row[1]
             cont = row[2]
             sql_execute("Insert into Best_seller(prodid ,name , Counter ) VALUES (%s , %s, %s)",[prodid,name,cont])


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    print("Content Filtering {Best Seller } is Done ")


best_seller()

def select_most_viewed_products():
    """ This function will Select & count every product from Tabel profiles previously viewed on the Postgres db """

    try:
        return sql_select("""SELECT profiles_previously_viewed.prodid, products.name,
                        COUNT(*)
                        FROM profiles_previously_viewed
                        INNER JOIN products ON profiles_previously_viewed.prodid = products.id
                        GROUP BY prodid ,products.name 
                        ORDER BY COUNT(*) DESC ; """)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



def most_viwed_products():
    """This function will Create Tabel Most viwed products on the Postgres db  """
    try:
        sql_query("DROP TABLE IF EXISTS most_viwed_products CASCADE")

        sql_query("""CREATE TABLE most_viwed_products                          
                        (prodid VARCHAR PRIMARY KEY,                  
                          name VARCHAR,                                 
                          Counter INTEGER ,                             
                          FOREIGN KEY (prodid) REFERENCES products(id));""")

        commit()

        results = select_most_viewed_products()

        #Right , now we can insert the result into the Tabel

        for row in results:
            prodid = row[0]
            name = row[1]
            cont = row[2]
            sql_execute("Insert into most_viwed_products(prodid ,name , Counter ) VALUES (%s , %s, %s)",[prodid,name,cont])
            commit()

    except(Exception, psycopg2.DatabaseError) as error:

        print(error)

    print("Content Filtering {Most viwed products } is Done ")



most_viwed_products()




#                                                                                  >> { Collaborative Filtering } <<<

def select_profiels_types_bouncer_and_browser():
    """This fuction will Select & filter the types of profiels on the Postgres db """
    bouncer_list = []
    BROWSER_list = []
    try:


        result = sql_select("""SELECT profiles.id, profiles.segment,profiles_previously_viewed.prodid, products.name  
                    
                        FROM profiles
                        INNER JOIN profiles_previously_viewed ON profiles.id = profiles_previously_viewed.profid
                        INNER JOIN products on profiles_previously_viewed.prodid = products.id
                        GROUP BY  profiles.id, profiles.segment ,profiles_previously_viewed.prodid ,products.name ;""")
       #We Got More then BOUNCER , BROWSER and BUYER but i fillterd the profiels on that

        for row in result:
            if row[1] == "BOUNCER" :
                # index [1] is The Segment !
                bouncer_list.append(row)
                continue


            elif result[1] == "BROWSER":
                BROWSER_list.append(row)
                continue


        return bouncer_list , BROWSER_list

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def profiels_types_bouncer_and_browser():
     """ This function will create Tabels for different types of profiels on the Postgres db """


     try:
         sql_query("DROP TABLE IF EXISTS profiels_type_browsers CASCADE")

         sql_query("DROP TABLE IF EXISTS profiels_type_boucer CASCADE")

         #One For BROWSERS types

         sql_query("""CREATE TABLE profiels_type_browsers 
                        (profid VARCHAR , 
                         prodid VARCHAR ,
                         product_name VARCHAR , 
                         segment VARCHAR ,
                         FOREIGN KEY (prodid) REFERENCES products(id),
                         FOREIGN KEY (profid) REFERENCES profiles(id));""")

         #And one for BOUNCERS types

         sql_query("""CREATE TABLE profiels_type_boucer                 
                       (profid VARCHAR ,                                   
                        prodid VARCHAR ,                                   
                        product_name VARCHAR ,                             
                        segment VARCHAR ,                                  
                        FOREIGN KEY (prodid) REFERENCES products(id),      
                        FOREIGN KEY (profid) REFERENCES profiles(id));""")

         commit()

         
         bouncer , BROWSER = select_profiels_types_bouncer_and_browser()

         #Inserting the data into the tabels

         for row in bouncer :
             profid = row[0]
             segment = row[1]
             prodid = row[2]
             name = row[3]
             sql_execute("Insert into profiels_type_boucer(profid ,segment , prodid, product_name) VALUES (%s , %s, %s, %s)",[profid,segment,prodid , name])
             commit()


         for row0 in BROWSER :

             profid1 = row0[0]
             segment1 = row0[1]
             prodid1 = row0[2]
             name1 = row0[3]
             sql_execute("Insert into profiels_type_browsers(profid ,segment , prodid, product_name  ) VALUES (%s , %s, %s, %s)",[profid1,segment1,prodid1 , name1])
             commit()

     except (Exception, psycopg2.DatabaseError) as error:

            print(error)

     print("Collaborative Filtering {profiels_type_browsers & bouncers} are Done ")


profiels_types_bouncer_and_browser()

def select_profiels_type_buyer():
    """This fuction will Select & filter the type BUYER profiels the Postgres db """

    try:
        return sql_select("""SELECT sessions.id, sessions.profid,sessions.segment, orders.prodid, products.name  

            FROM sessions
            INNER JOIN orders ON sessions.id = orders.sessionsid
            INNER JOIN products on orders.prodid = products.id
            GROUP BY sessions.id, sessions.profid,orders.prodid, products.name, sessions.segment ;
             """)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def profiels_type_buyer():

    """ This function will create profiels type buyer for  on the Postgres db """

    try:

        sql_query("DROP TABLE IF EXISTS profiels_type_buyer CASCADE")
        commit()

        sql_query("""CREATE TABLE profiels_type_buyer                                                                                                               
                         (profid VARCHAR ,                                                                                                                            
                         prodid VARCHAR ,                                                                                                                             
                         product_name VARCHAR ,                                                                                                                       
                         segment VARCHAR ,                                                                                                                            
                         FOREIGN KEY (prodid) REFERENCES products(id),                                                                                                
                         FOREIGN KEY (profid) REFERENCES profiles(id)); """)
        commit()


        BUYER = select_profiels_type_buyer()
        for row in BUYER :
            profid1 = row[1]
            segment1 = row[2]
            prodid1 = row[3]
            name1 = row[4]
            sql_execute("Insert into profiels_type_buyer(profid ,segment , prodid, product_name  ) VALUES (%s , %s, %s, %s)",[profid1,segment1,prodid1 , name1])

        commit()

    except (Exception, psycopg2.DatabaseError) as error :
        print(error)

    print("Collaborative Filtering {profiels_type_buyer} is Done ")


profiels_type_buyer()




""" TEST !! """





print("Content-Based Filtering \n")


print("Populair bij op = op \n")
print(sql_select("""SELECT prodid , name  
            FROM BEST_seller
            WHERE Counter > 1000
            LIMIT 4; """),"\n")

print("Andere kijken ook \n")
print(sql_select(""" SELECT prodid , name
                        FROM most_viwed_products
                        WHERE Counter > 5000
                        LIMIT 4; """), "\n")


print("Collaborative Filtering \n ")

print(" U kan de ID {5a394475ed29590001038e43} gebruiken Voor {BUYER} \n en ID {59dce40ea56ac6edb4c37dfd} gebruiken Voor {BOUNCER} \n En ID {59dce40ea56ac6edb4c37df5} Voor {BROWSER}  ")

IDp = input("Voer Eem ID in ")

if IDp == "5a394475ed29590001038e43" :
    print("BUYER Type")
    print(sql_select("""SELECT prodid , product_name       
                     FROM profiels_type_buyer
                     LiMIT 4 ;"""))

elif IDp == "59dce40ea56ac6edb4c37dfd":
    print("BOUNCER TYPE ")
    print(sql_select("""SELECT prodid , product_name
                     FROM profiels_type_boucer
                     LiMIT 4 ;"""))

elif IDp == "59dce40ea56ac6edb4c37df5":
    print("BROWSER TYPE")
    print(sql_select("""SELECT prodid , product_name    
                     FROM profiels_type_browsers  
                     LiMIT 4 ;"""))