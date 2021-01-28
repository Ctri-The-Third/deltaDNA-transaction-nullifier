# deltaDNA transaction nullifier

deltaDNA is an analytics platform primarily aimed for empowered mobile games developers to have data driven understanding of their games, and to engage with their users.

## App Purpose
To take an identified event from our analytics platform, and provide a negative value of revenue equal to that in the identified event, resulting in a effective value of 0 during SUM aggregations  of revenue.

## Installation 

Clone the repository to a directory of youor choosing.
Required Packages: 

`pending`

### settings.json

In order for repeat usage of the nullifier, it is necessary to load some configuration data into a settings file.
In the same directory as the script files, create a `settings.json` file with the following fields
```
{
    "user": "user@domain.com",
    "db": "accountName.gameName", 
    "collectURL":"https://collect??????.deltadna.net/collect/api",
    "collectKey":"501982???????????????4625"
}
```

Make sure you fill user and db fields with your deltadna login credentials (for fetching analytics data about your game via Direct Access) and the collectURL and collectKey with the details for sending events to the platform for the matching game via our Rest APIs

![note, screenshot here]()

### input.csv

