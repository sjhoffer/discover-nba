import urllib.request as url
import numpy as np

class PlayerID(object):
    """Combs through list of possible NBA player IDs on ESPN.com's game log site.  
    Returns those IDs that have matching active players.  Object contains the following
    properties:
    
    base_url: URL to comb.
    url_redirect: array containing the list of possible player IDs in the first column, and 
    flag indicating whether or not the player IDs in question have player profiles or not.
    """
    
    def __init__(self,base_url,size):
        """Returns PlayerID object containing the below indicated base URL.  Also generates 
        array of zeros in the shape of our url_redirect attribute.  The row count is the
        max end of the range we will be searching over
        """
        
        self.base_url = base_url # example URL is "http://www.espn.com/nba/player/_/id"
        self.size = size
        self.url_redirect = np.zeros((size,2))
        
    def generate_urls(self):
        """For each test player ID, appends test ID to base URL and then creates a request object.
        Following this, the request URL is opened.  The output URL is then tested against the base
        URL to check whether or not there was a page redirect.  If there was a redirect, mark the
        second column of url_redirect with a 2.  If there was no redirect, mark the second column with 1.
        """
        
        for player_id_attempt in range(self.size):
            
            test_url = self.base_url + str("/" + str(player_id_attempt))
            
            request = url.Request(test_url)
            response = url.urlopen(request)
            
            if test_url == response.geturl():
                self.url_redirect[player_id_attempt][0] = player_id_attempt
                self.url_redirect[player_id_attempt][1] = 1
                
                print("I found a player at this address (" + str(player_id_attempt) + "). Currently " \
                 + str(round(100*player_id_attempt/self.size,2)) + "% through processing.")
                
            else:
                self.url_redirect[player_id_attempt][0] = player_id_attempt
                self.url_redirect[player_id_attempt][1] = 2
               
                print("I didn't find player at this address (" + str(player_id_attempt) + "). Currently " \
                 + str(round(100*player_id_attempt/self.size,2)) + "% through processing.")
                
        return url_redirect[np.where(url_redirect == 1)]

