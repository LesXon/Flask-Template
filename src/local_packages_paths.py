# Paquetes Generales
import sys

class LocalPackagesPaths:
   """
   Objectives:
   - Configures the environment variables of the local packages used in the app
   """   

   def __init__(self,platform:str):
       """             
       Parameters:
       - platform.. : Platform used to deploy the application
                      platform ='colab'
                      platform ='deepnote'
                      platform ='windows'
                      platform ='linux'                      

       Objectives:
       - Initialization
  
       Returns:
       - None
       """       

       self.platform = platform

       self.paths()

   def paths(self)->None:

       if self.platform == 'colab':
          path_platform = "/content/drive/My Drive/Colab_Notebooks" 

       elif self.platform == 'deepnote':
          path_platform = "/content/drive/My Drive/Colab_Notebooks"

       elif self.platform == 'drive':
          path_platform = "/Colab_Notebooks"

       elif self.platform == 'windows':
          path_platform = ".."
          
       elif self.platform == 'linux':
          path_platform = "pendiente"

       sys.path.append(path_platform+'/dev/lesxon/py/libs')
       sys.path.append(path_platform+'/dev/lesxon/py/libs/erm/design/xlsx')

       sys.path.append('src')

       sys.path.append('blueprints/home/src')     
       
       return None

