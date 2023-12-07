#----------------------> DATA Collection Engine <-----------------------#

# Data Collection Engine Functionality
# Collects Data from the user
# Formats it correctly
# Sends it over the data pipelines
# Employs mechanisms to make sure the data has been sent and received
# Employs a data modification process, to clean , organize and keep data uptodate

class Data_Collection_Engine:

     User_Profile={

        "user_age":"",
        "user_education":"",
        "user_profession":"",
        "user_gender":""
    }

     Device_Data={

        "device":"",
        "device_type":"",
        "device_O.S":"",

    }

     Types_Of_Data={

        "Photos": "",
        "videos": "",
        "documents": "",
        "apps":""

    }
     
# function collects data for user_profile creation
     def user_profile(self):

        # This function collects data to build user profile
        # Details collected help form a user Profile to optimize responses to 
        # to user personal needs 

        for key in self.User_Profile:
             print("Enter %s"%key)
             self.User_Profile[key]=str(input())

# function collects data for device_profile creation
     def user_device_data(self):

         # This function collects data for identify the device 
        
        for key in self.Device_Data:
            
          print("Enter %s"%key)
          self.Device_Data[key]=str(input())
                                    
           
     
  
# function collects data for user_data_profile creation
     def types_of_data(self):

        # This function collects the responses about the types of data the user has / uses 
        # on their smart device

        for key in self.Types_Of_Data:

            print("Do you use  %s ?"%key)
            self.Types_Of_Data[key]=str(input())
     
    

function_caller= Data_Collection_Engine()
Data_Display = Data_Collection_Engine()

function_caller.user_profile()       
function_caller.user_device_data()
function_caller.types_of_data()  

print(Data_Display.User_Profile)
print(Data_Display.Device_Data)
print(Data_Display.Types_Of_Data)

class Query_Engine:

    data_collected=Data_Collection_Engine()