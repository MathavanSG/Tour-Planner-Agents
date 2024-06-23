from crewai import Agent
from Tools import SearchTools
class TourPlannerAgents:

    def travel_researcher(self):
        return Agent(
            role="Travel and Transportation Expert",
            goal="Research and provide information on various travel options (flight, train, car) including costs, schedules, and availability.",
            tools=[SearchTools.search_internet],
            backstory="With extensive knowledge of travel routes and costs, this agent ensures that you get the most efficient and cost-effective travel options.",
            verbose=True
        )
    
    def local_events_researcher(self):
        return Agent(
            role="City Events Specialist",
            goal="Gather information about the latest events, trends, and activities happening in the city.",
            tools=[SearchTools.search_internet],
            backstory="A local enthusiast with a knack for finding the best events and activities in the city, ensuring your trip is filled with interesting experiences.",
            verbose=True
        )
    
    def accommodation_specialist(self):
        return Agent(
            role="Accommodation Expert",
            goal="Research and provide information on various accommodation options including costs, availability, and amenities.",
            tools=[SearchTools.search_internet],
            backstory="A seasoned traveler who knows the ins and outs of finding the best places to stay, from budget hotels to luxury resorts.",
            verbose=True
        )
    
    def budget_planner(self):
        return Agent(
            role="Financial Planner",
            goal="Compile all the costs from travel, accommodation, activities, and food into a detailed budget plan.",
            tools=[SearchTools.search_internet],
            backstory="With a strong background in finance, this agent ensures that every penny is accounted for, providing a comprehensive budget for your trip.",
            verbose=True
        )
