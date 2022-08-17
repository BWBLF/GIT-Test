"""
Zombie Dice Bots

Trò chơi lập trình là một thể loại trò chơi mà thay vì chơi trò chơi trực tiếp, người chơi viết các chương trình bot để chơi trò chơi
 đó một cách độc lập. Tôi đã tạo một trình mô phỏng Zombie Dice, cho phép các lập trình viên thực hành các kỹ năng của họ trong khi tạo 
 AI chơi trò chơi. Các bot Zombie Dice có thể đơn giản hoặc cực kỳ phức tạp, và rất phù hợp cho một bài tập trong lớp hoặc một thử thách
  lập trình cá nhân.

Zombie Dice là một trò chơi xúc xắc nhanh chóng, vui nhộn của Steve Jackson Games. Người chơi là những thây ma cố gắng ăn càng nhiều não
 người càng tốt mà không bị bắn ba lần. Có một cốc gồm 13 viên xúc xắc với các biểu tượng bộ não, bước chân và khẩu súng ngắn trên khuôn
  mặt của họ. Các biểu tượng xúc xắc được tô màu và mỗi màu có khả năng xảy ra mỗi sự kiện khác nhau. Mỗi con xúc xắc đều có hai mặt với
   bước chân, nhưng xúc xắc có biểu tượng màu xanh lá cây có nhiều mặt hơn với bộ não, xúc xắc biểu tượng màu đỏ có nhiều súng ngắn hơn và
    xúc xắc biểu tượng màu vàng có bộ não và súng ngắn chia đều. Thực hiện như sau trên mỗi lượt của người chơi:

Đặt tất cả 13 viên xúc xắc vào cốc. Người chơi rút ngẫu nhiên ba viên xúc xắc từ cốc và sau đó tung chúng. Người chơi luôn tung chính xác ba 
viên xúc xắc.
Họ đặt sang một bên và đếm bất kỳ bộ não nào (con người bị ăn não) và súng ngắn (con người đã chiến đấu chống lại). Tích lũy ba khẩu súng 
ngắn sẽ tự động kết thúc lượt của người chơi với không điểm (bất kể họ có bao nhiêu bộ não). Nếu họ có từ 0 đến hai khẩu súng ngắn, họ có 
thể tiếp tục lăn nếu họ muốn. Họ cũng có thể chọn kết thúc lượt của mình và thu về một điểm cho mỗi bộ não.
Nếu người chơi quyết định tiếp tục lăn, họ phải cuộn tất cả các viên xúc xắc bằng bước chân. Hãy nhớ rằng người chơi phải luôn tung ba viên
 xúc xắc; họ phải rút thêm xúc xắc ra khỏi cốc nếu có ít hơn ba bước chân để lăn. Một người chơi có thể tiếp tục tung xúc xắc cho đến khi họ
  nhận được ba khẩu súng ngắn — mất tất cả — hoặc tất cả 13 viên xúc xắc đã được tung. Người chơi không được chỉ cuộn lại một hoặc hai viên
   xúc xắc và không được dừng cuộn giữa chừng.
Khi ai đó đạt đến 13 bộ não, những người chơi còn lại sẽ kết thúc vòng đấu. Người có nhiều bộ não nhất sẽ thắng. Nếu hòa, các tay vợt bị hòa
 sẽ chơi một hiệp đấu tiebreak cuối cùng.
Zombie Dice có một cơ chế trò chơi vận động may rủi: bạn cuộn xúc xắc càng nhiều, bạn càng có thể nhận được nhiều bộ não, nhưng cuối cùng thì
 bạn càng có nhiều khả năng tích lũy được ba khẩu súng ngắn và mất tất cả. Khi một người chơi đạt được 13 điểm, những người chơi còn lại sẽ có
  thêm một lượt nữa (để có thể bắt kịp) và trò chơi kết thúc. Người chơi với số điểm cao nhất sẽ chiến thắng. Bạn có thể tìm thấy các quy tắc 
  đầy đủ tại https://github.com/asweigart/zombiedice/ .

Cài đặt mô-đun zombiedice với pip bằng cách làm theo hướng dẫn trong Phụ lục A.
 Bạn có thể chạy bản demo của trình mô phỏng với một số bot được tạo sẵn bằng cách chạy như sau trong shell tương tác:
 import zombiedice
 #####
zombiedice.demo()
Zombie Dice Visualization is running. Open your browser to http://localhost:51810 to view it.
Press Ctrl-C to quit.
"""
import zombiedice

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)