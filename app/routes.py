from flask_smorest import Blueprint
from flask.views import MethodView

from app import db
from .models import User, Stack, Card, Fact, Clue
from .schemas import UserSchema, StackSchema, CardSchema


blp = Blueprint('root', __name__, url_prefix='/v1')


@blp.route('/users/<user_id>')
class UserById(MethodView):

    @blp.response(UserSchema)
    def get(self, user_id):
        user = db.session.query(User).get_or_404(user_id)
        return user


@blp.route('/stacks/<stack_id>')
class StackById(MethodView):

    @blp.response(StackSchema)
    def get(self, stack_id):
        stack = db.session.query(Stack).get_or_404(stack_id)
        return stack


@blp.route('/stacks/<stack_id>/cards')
class CardsByStackById(MethodView):

    @blp.response(CardSchema(many=True))
    def get(self, stack_id):
        stack = db.session.query(Stack).get_or_404(stack_id)
        cards = stack.cards
        return cards


@blp.route('/users/<user_id>/stacks')
class StacksByUserById(MethodView):

    @blp.response(StackSchema(many=True))
    def get(self, user_id):
        user = db.session.query(User).get_or_404(user_id)
        stacks = user.stacks
        return stacks


@blp.route('/recreatedb/')
def recreate():
    db.drop_all()
    db.create_all()

    # user and stack data
    user = User("jaydan")
    stack = Stack("colors")
    user.stacks.append(stack)
    db.session.add(user)
    db.session.add(stack)

    # card data
    red_card = Card(name="red")
    red_card.stacks.append(stack)
    db.session.add(red_card)

    blue_card = Card(name="blue")
    blue_card.stacks.append(stack)
    db.session.add(blue_card)

    orange_card = Card(name="orange")
    orange_card.stacks.append(stack)
    db.session.add(orange_card)

    # facts
    english_red_fact = Fact("red")
    zhongwen_red_fact = Fact("红")
    hanyu_red_fact = Fact("hóng")

    english_blue_fact = Fact("blue")
    zhongwen_blue_fact = Fact("蓝")
    hanyu_blue_fact = Fact("lán")

    english_orange_fact = Fact("orange")
    zhongwen_orange_fact = Fact("橙")
    hanyu_orange_fact = Fact("chéng")

    # clues
    english_red_clue = Clue([english_red_fact])
    zhongwen_red_clue = Clue([zhongwen_red_fact])
    hanyu_red_clue = Clue([hanyu_red_fact])

    english_blue_clue = Clue([english_blue_fact])
    zhongwen_blue_clue = Clue([zhongwen_blue_fact])
    hanyu_blue_clue = Clue([hanyu_blue_fact])

    english_orange_clue = Clue([english_orange_fact])
    zhongwen_orange_clue = Clue([zhongwen_orange_fact])
    hanyu_orange_clue = Clue([hanyu_orange_fact])

    # card data
    red_card.clues.append(english_red_clue)
    red_card.clues.append(zhongwen_red_clue)
    red_card.clues.append(hanyu_red_clue)
    red_card.facts.append(english_red_fact)
    red_card.facts.append(zhongwen_red_fact)
    red_card.facts.append(hanyu_red_fact)

    blue_card.clues.append(english_blue_clue)
    blue_card.clues.append(zhongwen_blue_clue)
    blue_card.clues.append(hanyu_blue_clue)
    blue_card.facts.append(english_blue_fact)
    blue_card.facts.append(zhongwen_blue_fact)
    blue_card.facts.append(hanyu_blue_fact)

    orange_card.clues.append(english_orange_clue)
    orange_card.clues.append(zhongwen_orange_clue)
    orange_card.clues.append(hanyu_orange_clue)
    orange_card.facts.append(english_orange_fact)
    orange_card.facts.append(zhongwen_orange_fact)
    orange_card.facts.append(hanyu_orange_fact)

    # commit the changes
    db.session.commit()
    return "created!"
