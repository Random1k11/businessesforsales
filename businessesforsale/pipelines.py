# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from businessesforsale.models import (db_connect, create_table, Businesses, check_existence_row_in_db,
                                    get_value_from_databse, update_values)
from scrapy.utils.project import get_project_settings



class BusinessesforsalePipeline(object):


    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        session = self.Session()
        BusinessesDB = Businesses()
        BusinessesDB.title        = item['title']
        BusinessesDB.location     = item['location']
        BusinessesDB.asking_price = item['asking_price']
        BusinessesDB.sales_revenu = item['sales_revenu']
        BusinessesDB.cash_flow    = item['cash_flow']
        BusinessesDB.currency     = item['currency']
        BusinessesDB.description  = item['description']
        BusinessesDB.details      = item['details']
        BusinessesDB.listing_id   = item['listing_id']
        BusinessesDB.URL          = item['URL']

        try:
            if check_existence_row_in_db(BusinessesDB.listing_id) == None:
                session.add(BusinessesDB)
                session.commit()
            columns_BusinessesDB = [i for i in dir(BusinessesDB) if not i.startswith('_') and i != 'metadata' and i != 'id' and i != 'details' and i != 'created_date'\
                                    and i != 'listing_id']
            if get_project_settings().get('UPDATE_VALUES_IN_DATABASE') == True:
                for column in columns_BusinessesDB:
                    if getattr(BusinessesDB, column) != getattr(get_value_from_databse(BusinessesDB.listing_id), column):
                        print(getattr(BusinessesDB, column), '||||', getattr(get_value_from_databse(BusinessesDB.listing_id), column))
                        result = [BusinessesDB.title, BusinessesDB.location, BusinessesDB.asking_price, BusinessesDB.sales_revenu, BusinessesDB.cash_flow, BusinessesDB.currency,
                                  BusinessesDB.description, BusinessesDB.listing_id, BusinessesDB.URL]
                        update_values(BusinessesDB.listing_id, result)
        except:
            session.rollback()
            raise
        finally:
            session.close()
