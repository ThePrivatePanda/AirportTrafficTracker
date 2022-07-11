class Flight:
    def __init__(
        self,
        departure_airport,
        arrival_airport,
        expected_departure_time,
        expected_arrival_time,
        flight_number,
        airline,
        aircraft,
        status,
        actual_departure_time,
        actual_arrival_time,
        gate,
        delay_reason
        ):
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.expected_departure_time = expected_departure_time
        self.expected_arrival_time = expected_arrival_time
        self.flight_number = flight_number
        self.airline = airline
        self.aircraft = aircraft
        self.status = status
        self.actual_departure_time = actual_departure_time
        self.actual_arrival_time = actual_arrival_time
        self.gate = gate
        self.delay_reason = delay_reason
        self.arrival_delay_minutes = self.get_arrival_delay_minutes()
        self.departure_delay_minutes = self.get_departure_delay_minutes()
    
    def get_departure_delay_minutes(self):
        pass
    def get_arrival_delay_minutes(self):
        pass
