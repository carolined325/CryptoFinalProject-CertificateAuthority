from psycopg import connect, sql
import csv

def for_2015(country:str, region: str, rank: int, score:int, stand_err:int, gdp: int, life_exp: int, freedom:int,  generosity: int, dystopia: int, trust:int, family:int):

    cmd=sql.SQL("INSERT INTO region (name) VALUES (%s) ON CONFLICT DO NOTHING;")
    args=(region,)
    curs.execute(cmd, args)
    conn.commit()


    cmd = sql.SQL("SELECT {} FROM {} where {} = {};")\
            .format(sql.Identifier('region_id'),\
                sql.Identifier('region'),\
                    sql.Identifier('name'),\
                        sql.Placeholder())
    args=(region,)
    curs.execute(cmd, args)
    region = curs.fetchall()
   

    region_id = [row[0] for row in region]
    region_id=str(region_id)
    region_id=region_id.replace('[','').replace(']','')

   
    
    cmd="""
        INSERT INTO country (name, region_id) VALUES ((%s),(%s));"""
    args=[country,region_id,]
    curs.execute(cmd, args)
    conn.commit()

    

    cmd = sql.SQL("SELECT {} FROM {} where {} = {};")\
            .format(sql.Identifier('c_id'),\
                sql.Identifier('country'),\
                    sql.Identifier('name'),\
                        sql.Placeholder())
    args=(country,)
    curs.execute(cmd, args)
    countryid = curs.fetchall()
 

    c_id = [row[0] for row in countryid]
    c_id=str(c_id)
    c_id=c_id.replace('[','').replace(']','')

 

    cmd="""
        INSERT INTO ranking (c_id,ranking, score, year) VALUES ((%s),(%s),(%s), 2015);"""
    args=[c_id,rank, score,]
    curs.execute(cmd, args)
    conn.commit()

    cmd="""SELECT rank_id FROM ranking WHERE ranking=(%s) AND c_id=(%s) AND score= (%s);"""
    args=[rank, c_id, score,]
    curs.execute(cmd, args)
    rankid=curs.fetchall()
   

    rank_id=[row[0] for row in rankid]
    rank_id=str(rank_id)
    rank_id=rank_id.replace('[','').replace(']','')

   

    cmd="""INSERT INTO stats (rank_id,stand_err, gdp, life_exp, freedom, generosity, dystopia, corruption, family) VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s));"""
    args=[rank_id,stand_err, gdp, life_exp, freedom, generosity, dystopia,trust, family]
    curs.execute(cmd, args)
    conn.commit()

def for_2016(country:str, region: str, rank: int, score:int, low_conf:int, up_conf:int, gdp: int, life_exp: int, freedom:int,  generosity: int, dystopia: int, trust:int, family:int):
    cmd=sql.SQL("INSERT INTO region (name) VALUES (%s) ON CONFLICT DO NOTHING;")
    args=(region,)
    curs.execute(cmd, args)
    conn.commit()


    cmd = sql.SQL("SELECT {} FROM {} where {} = {};")\
            .format(sql.Identifier('region_id'),\
                sql.Identifier('region'),\
                    sql.Identifier('name'),\
                        sql.Placeholder())
    args=(region,)
    curs.execute(cmd, args)
    region = curs.fetchall()
   

    region_id = [row[0] for row in region]
    region_id=str(region_id)
    region_id=region_id.replace('[','').replace(']','')

    
    
    cmd="""
        INSERT INTO country (name, region_id) VALUES ((%s),(%s)) ON CONFLICT DO NOTHING;"""
    args=[country,region_id,]
    curs.execute(cmd, args)
    conn.commit()

    

    cmd = sql.SQL("SELECT {} FROM {} where {} = {};")\
            .format(sql.Identifier('c_id'),\
                sql.Identifier('country'),\
                    sql.Identifier('name'),\
                        sql.Placeholder())
    args=(country,)
    curs.execute(cmd, args)
    countryid = curs.fetchall()
    

    c_id = [row[0] for row in countryid]
    c_id=str(c_id)
    c_id=c_id.replace('[','').replace(']','')

    

    cmd="""
        INSERT INTO ranking (c_id,ranking, score, year,low_conf, high_conf) VALUES ((%s),(%s),(%s), 2016, (%s), (%s));"""
    args=[c_id,rank, score,low_conf, up_conf]
    curs.execute(cmd, args)
    conn.commit()

    cmd="""SELECT rank_id FROM ranking WHERE ranking=(%s) AND c_id=(%s) AND score= (%s) AND year=2016;"""
    args=[rank, c_id, score,]
    curs.execute(cmd, args)
    rankid=curs.fetchall()
    

    rank_id=[row[0] for row in rankid]
    rank_id=str(rank_id)
    rank_id=rank_id.replace('[','').replace(']','')

   

    cmd="""INSERT INTO stats (rank_id, gdp, life_exp, freedom, generosity, dystopia, corruption, family) VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s));"""
    args=[rank_id, gdp, life_exp, freedom, generosity, dystopia,trust, family]
    curs.execute(cmd, args)
    conn.commit()

def for_2017(country:str,rank:str,score:int,whisk_high:int, whisk_low:int, gdp:int, family:int, life_exp:int, freedom:int, trust:int, generosity:int, dystopia:int):
    
    cmd="""
        INSERT INTO country (name) VALUES ((%s)) ON CONFLICT DO NOTHING;"""
    args=[country,]
    curs.execute(cmd, args)
    conn.commit()

    

    cmd = sql.SQL("SELECT {} FROM {} where {} = {};")\
            .format(sql.Identifier('c_id'),\
                sql.Identifier('country'),\
                    sql.Identifier('name'),\
                        sql.Placeholder())
    args=(country,)
    curs.execute(cmd, args)
    countryid = curs.fetchall()
    

    c_id = [row[0] for row in countryid]
    c_id=str(c_id)
    c_id=c_id.replace('[','').replace(']','')


    cmd="""
        INSERT INTO ranking (c_id,ranking, score, year) VALUES ((%s), (%s),(%s),2017);"""
    args=(c_id,rank,score, )
    curs.execute(cmd, args)
    conn.commit()

    cmd="""SELECT rank_id FROM ranking WHERE ranking=(%s) AND c_id=(%s) AND score= (%s) AND year=2017;"""
    args=[rank, c_id, score,]
    curs.execute(cmd, args)
    rankid=curs.fetchall()
    

    rank_id=[row[0] for row in rankid]
    rank_id=str(rank_id)
    rank_id=rank_id.replace('[','').replace(']','')

    cmd="""INSERT INTO stats (whisker_high, whisker_low,rank_id, gdp, life_exp, freedom, generosity, dystopia, corruption, family) VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s));"""
    args=[whisk_high, whisk_low, rank_id, gdp, life_exp, freedom, generosity, dystopia,trust, family]
    curs.execute(cmd, args)
    conn.commit()

def for_2018(country:str,rank:str,score:int, gdp:int, social_supp:int, life_exp:int, freedom:int, generosity:int, corruption:int):
    cmd="""
        INSERT INTO country (name) VALUES ((%s)) ON CONFLICT DO NOTHING;"""
    args=[country,]
    curs.execute(cmd, args)
    conn.commit()

    

    cmd = sql.SQL("SELECT {} FROM {} where {} = {};")\
            .format(sql.Identifier('c_id'),\
                sql.Identifier('country'),\
                    sql.Identifier('name'),\
                        sql.Placeholder())
    args=(country,)
    curs.execute(cmd, args)
    countryid = curs.fetchall()
    

    c_id = [row[0] for row in countryid]
    c_id=str(c_id)
    c_id=c_id.replace('[','').replace(']','')


    cmd="""
        INSERT INTO ranking (c_id,ranking, score, year) VALUES ((%s), (%s),(%s),2018);"""
    args=(c_id,rank,score, )
    curs.execute(cmd, args)
    conn.commit()

    cmd="""SELECT rank_id FROM ranking WHERE ranking=(%s) AND c_id=(%s) AND score= (%s) AND year=2018;"""
    args=[rank, c_id, score,]
    curs.execute(cmd, args)
    rankid=curs.fetchall()
    

    rank_id=[row[0] for row in rankid]
    rank_id=str(rank_id)
    rank_id=rank_id.replace('[','').replace(']','')

    if(corruption=='N/A'):
        cmd="""INSERT INTO stats (social_support,rank_id, gdp, life_exp, freedom, generosity) VALUES ((%s),(%s),(%s),(%s),(%s),(%s));"""
        args=(social_supp, rank_id, gdp, life_exp, freedom, generosity,)
    else:
        cmd="""INSERT INTO stats (social_support,rank_id, gdp, life_exp, freedom, generosity, corruption) VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s));"""
        args=[social_supp, rank_id, gdp, life_exp, freedom, generosity, corruption,]
    curs.execute(cmd, args)
    conn.commit()

def for_2019(country:str,rank:str,score:int, gdp:int, social_supp:int, life_exp:int, freedom:int, generosity:int, corruption:int):
    cmd="""
        INSERT INTO country (name) VALUES ((%s)) ON CONFLICT DO NOTHING;"""
    args=[country,]
    curs.execute(cmd, args)
    conn.commit()

    

    cmd = sql.SQL("SELECT {} FROM {} where {} = {};")\
            .format(sql.Identifier('c_id'),\
                sql.Identifier('country'),\
                    sql.Identifier('name'),\
                        sql.Placeholder())
    args=(country,)
    curs.execute(cmd, args)
    countryid = curs.fetchall()
    

    c_id = [row[0] for row in countryid]
    c_id=str(c_id)
    c_id=c_id.replace('[','').replace(']','')

    print(c_id)

    cmd="""
        INSERT INTO ranking (c_id,ranking, score, year) VALUES ((%s), (%s),(%s),2019);"""
    args=(c_id,rank,score, )
    curs.execute(cmd, args)
    conn.commit()

    cmd="""SELECT rank_id FROM ranking WHERE ranking=(%s) AND c_id=(%s) AND score= (%s) AND year=2019;"""
    args=[rank, c_id, score,]
    curs.execute(cmd, args)
    rankid=curs.fetchall()
    

    rank_id=[row[0] for row in rankid]
    rank_id=str(rank_id)
    rank_id=rank_id.replace('[','').replace(']','')

    print(rank_id)


    cmd="""INSERT INTO stats (social_support,rank_id, gdp, life_exp, freedom, generosity, corruption) VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s));"""
    args=[social_supp, rank_id, gdp, life_exp, freedom, generosity, corruption,]
    curs.execute(cmd, args)
    conn.commit()


try:

    with connect("dbname=Project2 user=user password=password port=5432") as conn:
        with conn.cursor() as curs:
            with open('2015.txt', 'r',  encoding = 'utf-16') as f:
                happy = csv.reader(f, delimiter='\t') # assumes tab-delimited
                next(happy, None) # skip the header
                # process each row: course[0] contains term, course[1] contains class "CPSC2500", course[2] contains instructor
                for hap in happy:
                    if (hap[0]): # check for blank row
                        country = hap[0]
                        region = hap[1]
                        rank = hap[2]
                        score= hap[3]
                        stand_err=hap[4]
                        gdp=hap[5]
                        family=hap[6]
                        life_exp=hap[7]
                        freedom=hap[8]
                        trust=hap[9]
                        generosity=hap[10]
                        dystopia=hap[11]
                        for_2015(country,region,rank,score,stand_err,gdp,life_exp,freedom,generosity,dystopia,trust, family)
            with open('2016.txt', 'r',  encoding = 'utf-16') as f:
                happy = csv.reader(f, delimiter='\t') # assumes tab-delimited
                next(happy, None) # skip the header
                # process each row: course[0] contains term, course[1] contains class "CPSC2500", course[2] contains instructor
                for hap in happy:
                    if (hap[0]): # check for blank row
                        country = hap[0]
                        region = hap[1]
                        rank = hap[2]
                        score= hap[3]
                        low_conf=hap[4]
                        up_conf=hap[5]
                        gdp=hap[6]
                        family=hap[7]
                        life_exp=hap[8]
                        freedom=hap[9]
                        trust=hap[10]
                        generosity=hap[11]
                        dystopia=hap[12]
                        for_2016(country,region,rank,score,low_conf, up_conf, gdp, family, life_exp, freedom, trust, generosity, dystopia)
            with open('2017.txt', 'r',  encoding = 'utf-16') as f:
                happy = csv.reader(f, delimiter='\t') # assumes tab-delimited
                next(happy, None) # skip the header
                # process each row: course[0] contains term, course[1] contains class "CPSC2500", course[2] contains instructor
                for hap in happy:
                    if (hap[0]): # check for blank row
                        country = hap[0]
                        rank = hap[1]
                        score = hap[2]
                        whisk_high= hap[3]
                        whisk_low=hap[4]
                        gdp=hap[5]
                        family=hap[6]
                        life_exp=hap[7]
                        freedom=hap[8]
                        generosity=hap[9]
                        trust=hap[10]
                        dystopia=hap[11]
                        for_2017(country,rank,score,whisk_high, whisk_low, gdp, family, life_exp, freedom, trust, generosity, dystopia)
            with open('2018.txt', 'r',  encoding = 'utf-16') as f:
                happy = csv.reader(f, delimiter='\t') # assumes tab-delimited
                next(happy, None) # skip the header
                # process each row: course[0] contains term, course[1] contains class "CPSC2500", course[2] contains instructor
                for hap in happy:
                    if (hap[0]): # check for blank row
                        rank = hap[0]
                        country = hap[1]
                        score = hap[2]
                        gdp= hap[3]
                        social_supp=hap[4]
                        life_exp=hap[5]
                        freedom=hap[6]
                        generosity=hap[7]
                        corruption=hap[8]
                        for_2018(country,rank,score, gdp, social_supp, life_exp, freedom, generosity, corruption)
            with open('2019.txt', 'r',  encoding = 'utf-16') as f:
                happy = csv.reader(f, delimiter='\t') # assumes tab-delimited
                next(happy, None) # skip the header
                # process each row: course[0] contains term, course[1] contains class "CPSC2500", course[2] contains instructor
                for hap in happy:
                    if (hap[0]): # check for blank row
                        rank = hap[0]
                        country = hap[1]
                        score = hap[2]
                        gdp= hap[3]
                        social_supp=hap[4]
                        life_exp=hap[5]
                        freedom=hap[6]
                        generosity=hap[7]
                        corruption=hap[8]
                        for_2019(country,rank,score, gdp, social_supp, life_exp, freedom, generosity, corruption)
            
except Exception as e: 
    print(f"Error: {e}") 

finally:
    if conn:
        conn.close()
                