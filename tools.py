import requests as r
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re



def flatten(t):
    return [item for sublist in t for item in sublist]

hyperparams = {'train_files','dev_files', 'test_files', 'train_batch_size', 'dev_batch_size', 'test_batch_size', 'n_hidden', 'learning_rate','dropout_rate', 'epochs', 'lm_alpha','lm_beta'}
imp_hyperparams = {'train_batch_size', 'dev_batch_size', 'test_batch_size', 'n_hidden', 'learning_rate','dropout_rate', 'epochs', 'lm_alpha','lm_beta'}

def tup_dict(raw: list, filter: set) -> dict:
    return {key:value for key,value in raw if key in filter}


class Github(object):
    def __init__(self, username, token):
        '''
        Binds necessary variables for requests.
        All the objects are designed to return the response, NOT THE JSON.
        You can change this to incorporate error handling, but the responsibility is on the user if auth fails 
        or you run out of requests.
        '''
        self.base = "https://api.github.com"
        self.user = username 
        self.token = token
    def __parse_params(self, param_dict: dict) -> str:
        '''
        Turns a dictionary of requests into API parameters.
        e.g {"page":2, "per_page":100} -> "page=2&per_page=100"
        ''' 
        return "&".join(f'{key}={pair}' for key, pair in param_dict.items())

    def __get_page(self, link: str, param_dict: dict):
        '''
        Returns a page using the API. Typically:
        https://api.github.com/...
        :param link: String for the link to request.
        :param param_dict: Additional parameters to request, such as the page and number of items.
        '''        
        #return f'{base}/{link}?{self.__parse_params(param_dict)}'        
        
        return r.get(f'{self.base}/{link}?{self.__parse_params(param_dict)}',
         auth =  (self.user,self.token))
    
    
    def get_repo(self, repo: str, subpage: str = '', param_dict: dict = {}):
        '''
        Retrieves repository information as a dictionary.
        :param repo: Repository name of format Author/Repository
        :param subpage: A subpage, such as the releases, commits and so on. (Optional)
        '''
        return self.__get_page(f'repos/{repo}/{subpage}', param_dict)
    
    def repo_search(self, keyword: str, param_dict: dict = {}):
        return self.__get_page(f'search/repositories', {'q':keyword} | param_dict)


    def get_releases(self, repo: str, param_dict: dict = {}):
        '''
        Gets up to 30 releases (?) for a repository, if available.

        '''
        return self.get_repo(repo, 'releases', param_dict)

    def get_commits(self, repo: str, param_dict: dict = {}):
        '''
        Gets up to 30 commits for a repository.
        ''' 
        return self.get_repo(repo, 'commits', param_dict)
    
    def get_commit_diff(self, repo: str, sha: str): 
        '''
        Gets the commit diff information.
        ''' 
        return self.get_repo(repo, f'commits/{sha}')


    def retrieve(self, link: str):
        return self.__get_page(link,{})