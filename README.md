# How can you use this app ?
1. Install Docker and make sure its running then check your Docker file sharing settings
2. Clone this repository and go to its location using your CLI
3. Run docker-compose up and wait for the process to finish ( Customers loading from CSV takes 3 min ~ 4 min ) ( Longitude /Latitude loading takes 10 min using openstreetmap api )
4. Check these endpoints:
🔗http://127.0.0.1:8000/api/swagger/
🔗http://127.0.0.1:8000/api/customers/
🔗http://127.0.0.1:8000/api/customers/{id}
