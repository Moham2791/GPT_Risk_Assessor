from DataCollectionEngine import Data_Collection_Engine

# This class shapes, forms and improve the over all query creation process
class Query_Engine:

    
    # intializing  query engine
    # Purpose of query engine to form the most relevant queries for prompts
    # 
     def __init__(self) -> None:
           pass      
     x=Data_Collection_Engine()

          


     def generate_query(query):
        
            query_string_for_Profile_creation="This user is %s old.By education user is %s by profession user is %s by gender user is %s."
            query_string_for_Device_info_Profile_creation=" The users device is a %s. The device type is %s. The O.S it runs on is %s." 
            query_string_for_types_of_data=" The user does%s have Photos.The user does%s have videos. The user does%s have documents. The user does%s have apps." 
            
            query= query_string_for_Profile_creation + query_string_for_Device_info_Profile_creation + query_string_for_types_of_data
            return query
    
     
     def prompt_query_structure(self):
          
          question_feed=self.generate_query()
          
