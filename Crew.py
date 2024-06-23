import os
from datetime import datetime
import streamlit as st
from crewai import Crew, Process, Agent
from Agents import TourPlannerAgents
from Tasks import TourPlannerTasks
from Tools import SearchTools
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.title("Tour Planner")

    # Instantiate the agents and tasks classes
    agents = TourPlannerAgents()
    tasks = TourPlannerTasks()

    # UI for input
    starting_city = st.text_input("Enter the starting city:")
    destination_city = st.text_input("Enter the Destination city:")
    number_of_days = st.text_input("Enter number of days:")
    travel_date = st.date_input("Select the travel date:", min_value=datetime.today())
    submit = st.button("Plan Tour")

    if submit and starting_city and destination_city and number_of_days:
        try:
            number_of_days = int(number_of_days)  # Validate and convert to integer
            current_date = travel_date.strftime("%Y-%m-%d")

            # Create the agents
            travel_researcher_agent = agents.travel_researcher()
            local_events_researcher_agent = agents.local_events_researcher()
            accommodation_specialist_agent = agents.accommodation_specialist()
            budget_planner_agent = agents.budget_planner()

            # Create the tasks
            travel_options_task = tasks.travel_options_research(travel_researcher_agent, starting_city, destination_city, number_of_days)
            local_events_task = tasks.local_events_activities_research(local_events_researcher_agent, starting_city, destination_city, current_date)
            accommodation_task = tasks.accommodation_research(accommodation_specialist_agent, starting_city, destination_city, number_of_days)
            budget_task = tasks.comprehensive_budget_planning(budget_planner_agent, starting_city, destination_city, number_of_days)

            # Form the crew
            tour_planner_crew = Crew(
                agents=[
                    travel_researcher_agent,
                    local_events_researcher_agent,
                    accommodation_specialist_agent,
                    budget_planner_agent
                ],
                tasks=[
                    travel_options_task,
                    local_events_task,
                    accommodation_task,
                    budget_task
                ],
                process=Process.sequential  # Optional: Sequential task execution is default
            )

            # Kick off the process
            result = tour_planner_crew.kickoff(inputs={'destination_city': destination_city, 'number_of_days': number_of_days, 'current_date': current_date})
            


        except ValueError:
            st.error("Number of days should be an integer.")

if __name__=="__main__":
    main()
