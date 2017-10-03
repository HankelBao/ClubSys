# Suzhou Foreign Language School Club Manage System
> There are always lack of such a system that can help monitor the whole club system.
> There are groups of people managing the whole club, but people rarely truly know about them and people are blind about how active clubs are raising their agenda and what they nowadays are doing.
> The system is right going to solve the problem.

## What this system is going to do:
* Introduce Clubs / See Activities and Ranks of Clubs / Get Links or Contact with Clubs
* Register Clubs / Register Club Activities and Ask for Rooms / Register to be members

## What tech the system is going to use:
* Flask + MongoDB as back end
* Vue.js as front end

## Design of Database
    COLLECTION Clubs: {
        _id
        name
        register_year
        description
        member: ARRAY COLLECTION {
            _id
            name
        }
        activities: ARRAY COLLECTION {
            _id
            description
        }
    }
    COLLECTION Members: {
        _id
        sys_id
        clubs: ARRAY COLLECTION {
            _id
            name
        }
    }
    COLLECTION Activities: {
        _id
        name
        date
        club_id
        club_name
        members: ARRAY COLLECTION {
            _id
            name
        }
    }