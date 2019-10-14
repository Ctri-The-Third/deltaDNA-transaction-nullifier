# deltaDNA transaction nullifier

deltaDNA is an analytics platform primarily aimed for empowered mobile games developers to have data driven understanding of their games, and to engage with their users.

## App Purpose
Sometimes if transaction validation isn't being employed then hackers will be able to falsify purchases to get in-game benefits or content they shouldn't. 
Whilst the deltaDNA platform doesn't protect against this, it does allow you to validate transactions against Google Play and the App Store, and to exclude invalid transactions from reporting. 

However, since the feature (and its benefits) aren't always apparent until _after_ you notice impossible spikes in your revenue graphs that it becomes apparent.

To get around the this, the app will identify aberrant transactions and submit matching events to the platform with an inverse revenue amount. Since all the aggregation and charts is based on SUMs, this flattens data back out.

## Installation 

