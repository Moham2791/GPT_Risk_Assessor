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

  

    # Collect user age, gender, education and profession.
    # this function uses a process to collect data from the user 
    # Data Fields : Device info, o.s type
    # Types of Data: Photos , videos ,docuemnts apps
    # Types of operations : User interactivity, number of users, types of users, utility of gadget (This process is subject to continouus
    # development and improvement)

     number_of_fields=len(User_Profile)

     def user_device_data(self):

         # This function collects data for identify the device 
        
        for i in self.Device_Data.keys:
            
          self.Device_Data.values=str(input())
                                     
        print(self.User_Profile)


        
     def user_profile(self,user):

        # This function collects data to build user profile
        # Details collected help form a user Profile to optimize responses to 
        # to user personal needs 

        for i in self.User_Profile:
            self.Device_Data.values=str(input())
         

     def types_of_data(self):

        # This function collects the responses about the types of data the user has / uses 
        # on their smart device

        for i in self.Types_Of_Data:
            self.Types_Of_Data.values=str(input())




        self.user_profile()       
        self.user_device_data()
        self.types_of_data()  