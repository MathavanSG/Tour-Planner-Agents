from textwrap import dedent
from crewai import Task

class TourPlannerTasks:

    def travel_options_research(self, agent,start_city, destination_city, number_of_days):
        return Task(
            description=dedent(f"""
                Research various travel options to the destination city, including flights, trains, and car rentals. Gather details on costs, schedules, and availability.
                Start city={start_city}
                Destination city: {destination_city}
                Number of days: {number_of_days}
            """),
            expected_output=dedent(f"""
                A report with detailed information on travel options, including costs and schedules, formatted as markdown.
                                   Note -The cost should be in INR currency
            """),
            agent=agent,
            async_execution=False,
            output_file='travel_options_report.md'
        )

    def local_events_activities_research(self, agent,start_city, destination_city, current_date):
        return Task(
            description=dedent(f"""
                Gather information about the latest events, activities, and trends in the destination city. Include details on costs, schedules, and any necessary reservations.
                Start city: {start_city}
                Destination city: {destination_city}
                Current date: {current_date}
            """),
            expected_output=dedent(f"""
                A report with detailed information on local events and activities, formatted as markdown.
                                   Note -The cost should be in INR currency
            """),
            agent=agent,
            async_execution=False,
            output_file='local_events_activities_report.md'
        )

    def accommodation_research(self, agent,start_city,destination_city, number_of_days):
        return Task(
            description=dedent(f"""
                Research various accommodation options in the destination city, including costs, availability, and amenities.
                Start city: {start_city}
                
                Destination city: {destination_city}
                Number of days: {number_of_days}
            """),
            expected_output=dedent(f"""
                A report with detailed information on accommodation options, formatted as markdown.
                                   Note -The cost should be in INR currency
            """),
            agent=agent,
            async_execution=False,
            output_file='accommodation_report.md'
        )

    def comprehensive_budget_planning(self, agent,start_city, destination_city, number_of_days):
        return Task(
            description=dedent(f"""
                Compile all the costs from travel, accommodation, activities, and food into a detailed budget plan. Ensure that every small cost is accounted for.
                Start city: {start_city}
                Destination city: {destination_city}
                Number of days: {number_of_days}
            """),
            expected_output=dedent(f"""
                A comprehensive budget report in INR, formatted as markdown.
            """),
            agent=agent,
            async_execution=False,
            output_file='comprehensive_budget_report.md'
        )
