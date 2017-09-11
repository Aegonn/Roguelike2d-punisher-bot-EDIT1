from TekkenGameState import TekkenGameState
from BasicCommands import BotCommands

class BotBehaviors:

    def Basic(gameState, botCommands):
        BotBehaviors.StopPressingButtonsAfterGettingHit(gameState, botCommands)
        BotBehaviors.GetUp(gameState, botCommands)
        BotBehaviors.TechCombos(gameState, botCommands)

    def StopPressingButtonsAfterGettingHit(gameState, botCommands):
        if gameState.IsBotStartedGettingHit():
            botCommands.ClearCommands()
        if gameState.IsBotStartedBeingThrown():
            botCommands.ClearCommands()

    def TechThrows(gameState, botCommands):
        if gameState.IsBotBeingThrown():
            botCommands.ThrowTech()

    def GetUp(gameState, botCommands):
        if gameState.IsBotOnGround():
            botCommands.ThrowTech()

    def TechCombos(gameState, botCommands):
        if gameState.IsBotBeingJuggled():
            botCommands.MashTech()

    def BlockAllAttacks(gameState: TekkenGameState, botCommands:BotCommands):
        if gameState.IsOppAttacking():
            if gameState.IsOppAttackLow():
                botCommands.LowParry(max(0, gameState.GetOppTimeUntilImpact()))
            else:
                botCommands.BlockMidFull(max(0, gameState.GetOppTimeUntilImpact()))
            if  gameState.IsOppAttackThrow():
                 botCommands.LowParry(max(0, gameState.GetOppTimeUntilImpact()))

    
   

   


    
          