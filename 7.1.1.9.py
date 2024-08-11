from manimlib.imports import *

class Rose(Scene):
    def construct(self):
        rose1 = ParametricFunction(
            lambda t: np.array([
                (np.cos(2*TAU*t))*(np.cos(0.5*TAU*t)),
                (np.cos(2*TAU*t))*(np.sin(0.5*TAU*t)),
                0
            ]),
            t_min=2.54*PI/64, t_max=7.625*PI/64, step_size=0.04, color=BLUE
        )
        rose1.set_fill(BLUE,opacity=0).scale(2.5).shift(0.5*LEFT+0.5*DOWN)
        rose2=rose1.copy().rotate(PI/2).shift(1.79*RIGHT+0.0*DOWN)
        ro1=VGroup(rose1,rose2)
        ro2=ro1.copy().rotate(PI).shift(1.78*UP+0.03*RIGHT)
        ros1=VGroup(ro1,ro2)
        ros2=ros1.copy().rotate(PI/4)
        ros1.set_fill(BLUE,opacity=0.5)
        self.play(ShowCreation(ros1),ShowCreation(ros2),run_time=1)
        self.wait(2)

        self.play(ApplyMethod(ros1.shift,3*LEFT),ApplyMethod(ros2.shift,3*RIGHT))
        self.wait(1)
        self.play(ApplyMethod(ros2.rotate,PI/4))
        self.play(ApplyMethod(ros2.shift,6*LEFT))
        self.wait(2)
        self.play(ApplyMethod(ros2.shift,6*RIGHT))
        self.play(ApplyMethod(ros2.rotate,PI/4))
        self.wait(1)

        txt=TextMobject("How many petals are filled =").to_edge(UP)
        self.play(ShowCreation(txt))
        self.wait(1)
        txt1=TextMobject("1",color=YELLOW_D).move_to(ros1.get_center()+1*RIGHT+1*UP)
        txt2=TextMobject("2",color=YELLOW_D).move_to(ros1.get_center()+1*RIGHT+1*DOWN)
        txt3=TextMobject("3",color=YELLOW_D).move_to(ros1.get_center()+1*LEFT+1*DOWN)
        txtt4=TextMobject("4",color=YELLOW_D).move_to(ros1.get_center()+1*LEFT+1*UP)
        self.play(ShowCreation(txt1))
        self.play(ShowCreation(txt2))
        self.play(ShowCreation(txt3))
        self.play(ShowCreation(txtt4))
        self.wait(1)
        self.play(FadeOut(txt1),FadeOut(txt2),FadeOut(txt3),ApplyMethod(txtt4.move_to,txt.get_center()+3.75*RIGHT))
        self.wait(1)

        txtt=TextMobject("The total number of petals = ").to_edge(DOWN)
        self.play(ShowCreation(txtt))
        self.wait(1)
        txt1=TextMobject("1",color=RED_D).move_to(ros1.get_center()+1*RIGHT+1*UP)
        txt2=TextMobject("2",color=RED_D).move_to(ros1.get_center()+1*RIGHT+1*DOWN)
        txt3=TextMobject("3",color=RED_D).move_to(ros1.get_center()+1*LEFT+1*DOWN)
        txt4=TextMobject("4",color=RED_D).move_to(ros1.get_center()+1*LEFT+1*UP)
        txt5=TextMobject("5",color=RED_D).move_to(ros2.get_center()+1.5*UP)
        txt6=TextMobject("6",color=RED_D).move_to(ros2.get_center()+1.5*RIGHT)
        txt7=TextMobject("7",color=RED_D).move_to(ros2.get_center()+1.5*DOWN)
        txt8=TextMobject("8",color=RED_D).move_to(ros2.get_center()+1.5*LEFT)
        self.play(ShowCreation(txt1))
        self.play(ShowCreation(txt2))
        self.play(ShowCreation(txt3))
        self.play(ShowCreation(txt4))
        self.play(ShowCreation(txt5))
        self.play(ShowCreation(txt6))
        self.play(ShowCreation(txt7))
        self.play(ShowCreation(txt8))
        self.wait(1)
        self.play(FadeOut(txt1),FadeOut(txt2),FadeOut(txt3),FadeOut(txt4),FadeOut(txt5),FadeOut(txt6),FadeOut(txt7),ApplyMethod(txt8.move_to,txtt.get_center()+3.75*RIGHT))
        self.wait(1)

        self.play(ApplyMethod(ros1.shift,3*RIGHT),ApplyMethod(ros2.shift,3*LEFT))
        self.wait(1)
        self.play(ApplyMethod(ros1.shift,2*LEFT),ApplyMethod(ros2.shift,2*LEFT))
        
        txt1=TextMobject("Fraction = ------- = --- ").next_to(ros2,2*RIGHT)
        self.play(ShowCreation(txt1))
        self.wait(1)
        self.play(FadeOut(txt),FadeOut(txtt),ApplyMethod(txtt4.move_to,txt1.get_center()+0.65*RIGHT+0.3*UP),ApplyMethod(txt8.move_to,txt1.get_center()+0.65*RIGHT+0.45*DOWN))
        self.wait(1)
        
        txt2=TextMobject("2*2*1",color=YELLOW_D).shift(txtt4.get_center())
        txt3=TextMobject("2*2*2",color=RED_D).shift(txt8.get_center())
        self.play(Transform(txtt4,txt2),Transform(txt8,txt3))
        self.wait(1)
        txt4=TexMobject("/").move_to(txt2.get_center()+0.5*LEFT)
        txt44=TexMobject("/").move_to(txt4.get_center()+0.5*RIGHT)
        txt5=TexMobject("/").move_to(txt3.get_center()+0.5*LEFT)
        txt55=TexMobject("/").move_to(txt5.get_center()+0.5*RIGHT)
        self.play(ShowCreation(txt4),ShowCreation(txt44),ShowCreation(txt5),ShowCreation(txt55))
        self.wait(1)
        txt6=TextMobject("1",color=YELLOW_D).move_to(txt2.get_center()+1.56*RIGHT)
        txt7=TextMobject("2",color=RED_D).move_to(txt3.get_center()+1.56*RIGHT)
        self.play(ShowCreation(txt6),ShowCreation(txt7))
        self.wait(2)
        