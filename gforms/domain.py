import json
from typing import List


class Resource:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url

    def __str__(self):
        return f"Resource(name={self.name}, url={self.url})"


class Activity:
    def __init__(self, time: str, activity: str, resources: List[Resource], recommendation: str):
        self.time = time
        self.activity = activity
        self.resources = resources
        self.recommendation = recommendation

    def __str__(self):
        resources_str = ', '.join(str(resource) for resource in self.resources)
        return f"Activity(time={self.time}, activity={self.activity}, resources=[{resources_str}], recommendation={self.recommendation})"


class DaySection:
    def __init__(self, name: str, activities: List[Activity]):
        self.name = name
        self.routine = activities

    def __str__(self):
        activities_str = ', '.join(str(activity) for activity in self.routine)
        return f"DaySection(name={self.name}, activities=[{activities_str}])"


class DaySchedule:
    def __init__(self, name: str, schedule: List[DaySection]):
        self.name = name
        self.schedule = schedule

    def __str__(self):
        schedule_str = ', '.join(str(section) for section in self.schedule)
        return f"DaySchedule(name={self.name}, schedule=[{schedule_str}])"


def create_resource(resource_data):
    return Resource(resource_data['name'], resource_data['url'])


def create_activity(activity_data):
    resources = [create_resource(res) for res in activity_data['resources']]
    return Activity(activity_data['time'], activity_data['activity'], resources, activity_data['recommendation'])


def create_day_section(section_data):
    activities = [create_activity(activity) for activity in section_data['routine']]
    return DaySection(section_data['name'], activities)


def create_day_schedule(schedule_data):
    schedule = [create_day_section(section) for section in schedule_data['schedule']]
    return DaySchedule(schedule_data['name'], schedule)


def deserialize_json(json_str) -> List[DaySchedule]:
    json_data = json.loads(json_str)
    return [create_day_schedule(day_schedule_data) for day_schedule_data in json_data]
