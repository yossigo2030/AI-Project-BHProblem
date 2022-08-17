
class Game:

    def __init__(self, curr_frame=0, visual=False):
        self.frame = curr_frame
        self.visual = visual
        self.board_ratio = pygame.display.get_window_size()
        self.player = Player.Player((board_ratio[0] / 2, board_ratio[1]),
                               r"resources\ship.png")
        self.wave = Wave.Wave(1, board_ratio)

    def update(self):
        self.frame += 1
        # player input and actions
        self.player.update()
        # enemy moves and actions
        Projectile.update_all()
        EnemyType.update_all()

        # Discard objects that are out of bounds
        Spriteables.sprite_culling()

        # check collisions
        player.set_score(collisionManager.collision_check_enemies())
        collisionManager.collision_check_player()
        # check pickup collisions

        # screen visual updates
        if self.visual:
            visual_update()
        #enemy spawning

        if self.wave.Update() == 1:
            self.wave = Wave.Wave(self.wave.number_of_wave+1, board_ratio)
        pygame.display.flip()

    def visual_update(self):
        Draw.redrawGameWindow()
        Projectile.draw_all()
        EnemyType.draw_all()
        self.player.draw()

    def