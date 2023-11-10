# Gaming the systems

[prev](./004_games_and_play.md)

## Systems

Systems are a form of game played among large groups of people. One such system we can consider is the global financial system. Citizens across nations spend time working in order to accumulate wealth and provide for their families and fund their luxuries. There are many other systems like this, and without listing too many examples, there are ways that this system can both be "gamed" and also ways that this system can work against its participants.

## Prisoners Dilemma

The prisoner's dilemma is a classic game that serves to analyze personal gain vs collective gain within a system. Consider the following hypothetical situation:

> You and your co-conspirator are on the black team and playing against the red team in a game of spies. You have been captured by the red team and have been placed in separate holding cells. You have two choices:
>
> * C: cooperate with your co-conspirator and keep your mouth shut
> * D: defect against your co-conspirator and tell the red team the plans
>
> If both of you cooperate (CC), then you both benefit a little bit from working together (+1 each)
>
> If both of you defect (DD), then you are both worse off because each one of you blabbed about the other (-1 each).
>
> If one of you defects and the other cooperates (CD), then the cooperator gets -2 and the defector gets +2.

A strategy can be formed between two players as the game is played multiple times, where each player remembers moves and outcomes of previous rounds.

### Strategies

#### Tit for Tat

The proven game-winning strategy to the above game is called "Tit for Tat". The algorithm is simple:

1. Cooperate first
2. Make the same move as your opponent did previously.

If everyone plays with this strategy, everyone cooperates, and everyone is better off. However, there are certain strategies that lead to a zero-sum payoff against tit for tat. One example would be the opposite:

1. Defect first
2. Make the same move as your opponent did previously.

We can see this play out below:

```text
CDCDCDCDCDCD
DCDCDCDCDCDC
```

Over the course of every two rounds, the total sum payoff is zero for both players. There has got to be a more beneficial strategy for all players. Ideally, the best strategies lead to long-term cooperation from both players.

#### Golden Strategy

The Golden Strategy is an enhanced approach to the Tit for Tat strategy. It is values-based. Here are the values held while employing this strategy:

1. Good intent. While a player may prioritize the self over the other player, needless harm is not beneficial.
2. Forgiveness. While a retaliation may be a great way to hold the other players accountable, retaliation leads to zero sum outcomes in long-term gameplay.
3. Trust that the opponent shares these values.

Here is the Golden algorithm

1. Cooperate first
2. Look back over the past two rounds. If there were more C's than D's, or an equal number from your opponent, then cooperate. Otherwise, defect.

Note that changing this algorithm to a defect first strategy will still be positive sum, because de-escalation is built into the algorithm.

## Take Aways

In the games we play, ideally we can learn from and teach one another, or engage in play and laugh together. The moment a game becomes a competition or has real-world consequences, it becomes a system.

If we bake de-escalation into our approaches to competitive gameplay, the systems we rely on can yield positive results. If we play long-term tit for tat, the game is zero sum.

Let's look for more positive sum strategies.

[prev](./004_games_and_play.md)
