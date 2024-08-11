# Parametric_Curves_rose
from manimlib.imports import *

class Rose(Scene):
    def construct(self):
        rose1 = ParametricFunction(
            lambda t: np.array([
                (np.cos(7*t))*(np.cos(t)),
                (np.cos(7*t))*(np.sin(t)),
                0
            ]),
            t_min=0, t_max=PI, step_size=0.04, color=BLUE
        )
        rose1.set_fill(BLUE,opacity=1).scale(1/2)

        rose2 = ParametricFunction(
            lambda t: np.array([
                (np.cos(7*t))*(np.cos(t)),
                (np.cos(7*t))*(np.sin(t)),
                0
            ]),
            t_min=0, t_max=PI, step_size=0.04, color=BLUE
        )
        rose2.scale(1/2)
        #self.play(ShowCreation(rose2))
        #self.wait(2)
        
        rect=Rectangle(height=4,width=5,color=BLUE)
        self.play(GrowFromCenter(rect))
        self.wait(1)
        f1=rose1.shift(1.75*LEFT+1.25*UP)
        f2=rose1.copy().next_to(f1)
        f3=rose1.copy().next_to(f2)
        f4=rose2.next_to(f3)
        f5=rose2.copy().shift(3.6*LEFT+1.25*DOWN)
        f6=rose2.copy().next_to(f5)
        f7=rose2.copy().next_to(f6)
        f8=rose2.copy().next_to(f7)
        f9=rose2.copy().shift(3.6*LEFT+2.5*DOWN)
        f10=rose2.copy().next_to(f9)
        f11=rose2.copy().next_to(f10)
        f12=rose2.copy().next_to(f11)
        f=VGroup(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12)
        self.play(ShowCreation(f))
        self.wait(1)

        self.play(ApplyMethod(f1.shift,1.8*RIGHT),ApplyMethod(f2.shift,0.6*RIGHT),ApplyMethod(f3.shift,0.6*LEFT),ApplyMethod(f4.shift,1.8*LEFT),ApplyMethod(f5 .shift,1.8*RIGHT),ApplyMethod(f6.shift,0.6*RIGHT),ApplyMethod(f7.shift,0.6*LEFT),ApplyMethod(f8.shift,1.8*LEFT),ApplyMethod(f9.shift,1.8*RIGHT),ApplyMethod(f10.shift,0.6*RIGHT),ApplyMethod(f11.shift,0.6*LEFT),ApplyMethod(f12.shift,1.8*LEFT))
        self.wait(1)
        self.play(ApplyMethod(f1.shift,1.25*DOWN),ApplyMethod(f2.shift,1.25*DOWN),ApplyMethod(f3.shift,1.25*DOWN),ApplyMethod(f4.shift,1.25*DOWN),ApplyMethod(f9.shift,1.25*UP),ApplyMethod(f10.shift,1.25*UP),ApplyMethod(f11.shift,1.25*UP),ApplyMethod(f12.shift,1.25*UP))
        self.wait(1)
        self.play(ApplyMethod(f1.shift,1.8*LEFT),ApplyMethod(f2.shift,0.6*LEFT),ApplyMethod(f3.shift,0.6*RIGHT),ApplyMethod(f4.shift,1.8*RIGHT),ApplyMethod(f5 .shift,1.8*LEFT),ApplyMethod(f6.shift,0.6*LEFT),ApplyMethod(f7.shift,0.6*RIGHT),ApplyMethod(f8.shift,1.8*RIGHT),ApplyMethod(f9.shift,1.8*LEFT),ApplyMethod(f10.shift,0.6*LEFT),ApplyMethod(f11.shift,0.6*RIGHT),ApplyMethod(f12.shift,1.8*RIGHT))
        self.wait(1)
        self.play(ApplyMethod(f1.shift,1.25*UP),ApplyMethod(f2.shift,1.25*UP),ApplyMethod(f3.shift,1.25*UP),ApplyMethod(f4.shift,1.25*UP),ApplyMethod(f9.shift,1.25*DOWN),ApplyMethod(f10.shift,1.25*DOWN),ApplyMethod(f11.shift,1.25*DOWN),ApplyMethod(f12.shift,1.25*DOWN))
        self.wait(1)

        txt=TextMobject("How many flowers are filled =").to_edge(UP)
        self.play(ShowCreation(txt))
        self.wait(1)
        txt1=TextMobject("1",color=YELLOW_D).move_to(f1.get_center())
        txt2=TextMobject("2",color=YELLOW_D).move_to(f2.get_center())
        txtt3=TextMobject("3",color=YELLOW_D).move_to(f3.get_center())
        self.play(ShowCreation(txt1))
        self.play(ShowCreation(txt2))
        self.play(ShowCreation(txtt3))
        self.wait(1)
        self.play(FadeOut(txt1),FadeOut(txt2),ApplyMethod(txtt3.move_to,txt.get_center()+3.75*RIGHT))
        self.wait(1)
        
        txtt=TextMobject("The total number of flowers = ").to_edge(DOWN)
        self.play(ShowCreation(txtt))
        self.wait(1)
        txt1=TextMobject("1",color=RED_D).move_to(f1.get_center())
        txt2=TextMobject("2",color=RED_D).move_to(f2.get_center())
        txt3=TextMobject("3",color=RED_D).move_to(f3.get_center())
        txt4=TextMobject("4",color=RED_D).move_to(f4.get_center())
        txt5=TextMobject("5",color=RED_D).move_to(f5.get_center())
        txt6=TextMobject("6",color=RED_D).move_to(f6.get_center())
        txt7=TextMobject("7",color=RED_D).move_to(f7.get_center())
        txt8=TextMobject("8",color=RED_D).move_to(f8.get_center())
        txt9=TextMobject("9",color=RED_D).move_to(f9.get_center())
        txt10=TextMobject("10",color=RED_D).move_to(f10.get_center())
        txt11=TextMobject("11",color=RED_D).move_to(f11.get_center())
        txt12=TextMobject("12",color=RED_D).move_to(f12.get_center())
        self.play(ShowCreation(txt1))
        self.play(ShowCreation(txt2))
        self.play(ShowCreation(txt3))
        self.play(ShowCreation(txt4))
        self.play(ShowCreation(txt5))
        self.play(ShowCreation(txt6))
        self.play(ShowCreation(txt7))
        self.play(ShowCreation(txt8))
        self.play(ShowCreation(txt9))
        self.play(ShowCreation(txt10))
        self.play(ShowCreation(txt11))
        self.play(ShowCreation(txt12))
        self.wait(1)
        self.play(FadeOut(txt1),FadeOut(txt2),FadeOut(txt3),FadeOut(txt4),FadeOut(txt5),FadeOut(txt6),FadeOut(txt7),FadeOut(txt8),FadeOut(txt9),FadeOut(txt10),FadeOut(txt11),ApplyMethod(txt12.move_to,txtt.get_center()+3.75*RIGHT))
        self.wait(1)
        
        self.play(ApplyMethod(f.shift,3*LEFT),ApplyMethod(rect.shift,3*LEFT))

        txt1=TextMobject("Fraction = ------- = --- ").next_to(rect,2*RIGHT)
        self.play(ShowCreation(txt1))
        self.wait(1)
        self.play(FadeOut(txt),FadeOut(txtt),ApplyMethod(txtt3.move_to,txt1.get_center()+0.65*RIGHT+0.3*UP),ApplyMethod(txt12.move_to,txt1.get_center()+0.65*RIGHT+0.45*DOWN))
        self.wait(1)
        
        txt2=TextMobject("3*1",color=YELLOW_D).shift(txtt3.get_center())
        txt3=TextMobject("2*2*3",color=RED_D).shift(txt12.get_center())
        self.play(Transform(txtt3,txt2),Transform(txt12,txt3))
        self.wait(1)
        txt4=TexMobject("/").move_to(txt2.get_center()+0.35*LEFT)
        txt5=TexMobject("/").move_to(txt3.get_center()+0.5*RIGHT)
        self.play(ShowCreation(txt4),ShowCreation(txt5))
        self.wait(1)
        txt6=TextMobject("1",color=YELLOW_D).move_to(txt2.get_center()+1.56*RIGHT)
        txt7=TextMobject("4",color=RED_D).move_to(txt3.get_center()+1.56*RIGHT)
        self.play(ShowCreation(txt6),ShowCreation(txt7))
        self.wait(2)
