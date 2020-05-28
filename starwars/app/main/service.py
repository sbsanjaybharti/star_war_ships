#!/usr/bin/env python3
"""
Import packages
"""
import collections

import json
from urllib.request import urlopen
from flask import current_app


class StarWarsAPI:
    """
    Class handle StarWars api
    """

    # /
    # Set Base class
    # Parameter None
    # class variable:
    #   api_url(string): get from ENV
    # /
    def __init__(self, category):
        self.api_url = current_app.config['STAR_WARS_API']
        self.category = category

    # /
    # Get Raw data
    # Parameter category
    # /
    def get_list(self, page=1):
        """
        Return list with detail
        """
        return json.loads(
            urlopen('{}/{}/?page={}'.format(self.api_url, self.category, int(page))).read()
        )

    # /
    # Get Raw data
    # Parameter id
    # Requirement: category_id, category_id_id
    # Return dict
    # /
    def get_single(self, category_id):
        """
        Description: get the detail of single category
        """
        return json.loads(
            urlopen('{}/{}/{}'.format(self.api_url, self.category, category_id)).read()
        )

class StarWars:
    """
    Class to filter data
    """
    def __init__(self):
        self.fields = {'name': 'name', 'hyperdrive_rating': 'hyperdrive'}
        self.__group_by_rating = collections.defaultdict(list)
        self.__group_by_null = []

    # / Get data
    # Requirement: None
    # Return dict
    # Description: Used to test variable data
    # /
    def get(self):
        """Test the return data of variable in unit test"""
        return {
            "starships": self.__group_by_rating,
            "starships_unknown_hyperdrive": self.__group_by_null
        }

    # / Get data
    # Requirement: data
    # Return dict
    # Description: Response as per the requirement. replacing key name
    # /
    def get_fields(self, data):
        """
        :param data:  {name:string, hyperdrive_rating: float}
        :return: {name:string, hyperdrive: float}
        """
        return {self.fields[i]: data[i] for i in self.fields.keys()}

    # / Get data
    # Requirement: data
    # Return dict
    # Description: Grouping the data to reduce the number of iteration
    # /
    def group(self, data):
        """
        group by hyperdrive_rating
        :param data: [
                    {name:string, hyperdrive_rating: float},
                     {name:string, hyperdrive_rating: float},...
                     ]
        :return: {
            hyperdrive_rating: [
                    {name:string, hyperdrive_rating: float},
                     {name:string, hyperdrive_rating: float}
                ],
            hyperdrive_rating: [
                    {name:string, hyperdrive_rating: float},
                    {name:string, hyperdrive_rating: float}
                ]
            ....
            }
        """
        if len(data) < 1:
            return self.__group_by_null
        current = data.pop()
        if current['hyperdrive_rating'] == 'unknown':
            self.__group_by_null.append(self.get_fields(current))
            return self.group(data)

        self.__group_by_rating[current['hyperdrive_rating']].append(self.get_fields(current))
        return self.group(data)

    # / Get list
    # Requirement: list
    # Return None
    # Description: Use to read all the pages of provided API service
    # /
    def page(self, lists, page=1):
        """
        recursive function view all pages
        :param list: current page list
        :param page: current page number
        :return:
        """
        if (lists['next'] is 'null') or (lists['next'] is None):
            self.group(lists['results'])
            return 'complete'

        self.group(lists['results'])
        self.page(StarWarsAPI('starships').get_list(page+1), page+1)

    # /
    # Requirement: None
    # Return object
    # Description: Task to perform
    # /
    def starships(self):
        """
        Used to data from API
        :return: process the data and return same object
        """
        self.page(StarWarsAPI('starships').get_list())
        return self

    # /
    # Requirement: None
    # Return dict
    # /
    def list(self):
        """
        arrange the data for response API
        :return: process the data and return same object
        """
        starships = []
        for key in sorted(self.__group_by_rating):
            starships.extend(self.__group_by_rating[key])
        return {
            "starships": starships,
            "starships_unknown_hyperdrive": self.__group_by_null
        }
