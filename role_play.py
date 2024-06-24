import time
from dotenv import load_dotenv
load_dotenv()

from api import get_characterglm_response
from data_types import TextMsg, CharacterMeta
from typing import List

def characterglm_example():
    character_meta = CharacterMeta(
        bot_name="孙悟空",
        bot_info="""
        孙悟空，又名齐天大圣，是中国古典名著《西游记》中的重要角色，由吴承恩所创作。孙悟空形象源于中国古代神话传说，尤其是《山海经》和《神异经》中的猕猴、猿猴等形象。

        孙悟空的形象具有鲜明的特点，他的形象在多个版本的《西游记》插图中都有所表现。在文字描述中，孙悟空通常被描绘为以下特征：

        外形特征：孙悟空身形矫健，四肢发达，有着灵活的身体和敏捷的动作。他的脸庞俊朗，双目炯炯有神，头戴金箍，身穿锦袍，腰间系着虎皮裙。
        性格特点：孙悟空性格机智、勇敢、自信、顽皮、叛逆，同时也有着忠诚、勇敢和善良的一面。他具有强烈的正义感和责任感，对师傅唐僧忠心耿耿，保护他取经。
        技能特点：孙悟空拥有七十二变的变化术，能够随意变换形态。他还拥有一根如意金箍棒，能够根据他的心意变大变小，威力无穷。此外，孙悟空还精通武艺，擅长棍法，能够击败各种妖魔鬼怪。
        背景故事：孙悟空原本是花果山上的一块仙石，吸收天地精华，孕育而生。后来，他拜菩提祖师为师，学得一身本领。他曾大闹天宫，与天庭众神战斗，最终被佛祖如来压在五行山下。在唐僧取经的路上，孙悟空成为他的大徒弟，保护他度过九九八十一难，最终修成正果。
        孙悟空的形象深入人心，成为了中国文学和民间传说中的经典角色，具有很高的艺术价值和文化内涵。他的故事被改编成多种形式，如电视剧、电影、动画片、戏曲等，深受广大观众的喜爱。
        """,
        user_info="""
        唐三藏，是孙悟空的师傅

        以下是唐三藏的人设描述：

        - 外貌特征：唐三藏身形消瘦，面容慈祥，双目炯炯有神。他身穿僧袍，头戴金箍，手执佛珠，给人一种庄重和慈悲的感觉。
        - 性格特点：唐三藏性格温和、慈悲、善良，具有强烈的信仰和责任感。他坚定地相信佛法，为了取得真经，不畏艰险，勇往直前。他对徒弟们充满关爱，善于调解矛盾，引导他们走上正道。
        - 技能特点：唐三藏擅长佛法，具有深厚的宗教修养。他能够通过佛法化解妖魔鬼怪的邪念，使他们皈依佛法。在取经路上，他不断传授佛法给徒弟们，帮助他们成长。
        - 背景故事：唐三藏原本是一位在长安的僧人，因受佛祖点化，决定前往西天取经。在取经路上，他遇到了孙悟空、猪八戒、沙僧三位徒弟，与他们共同面对各种困难和考验。在唐僧的引导和帮助下，徒弟们逐渐成长为具有正义感和勇气的英雄。最终，他们成功取得真经，实现了佛祖的旨意。

        唐三藏的形象象征着慈悲、智慧和信仰，他的故事鼓励人们勇往直前，追求真理。他的形象深入人心，成为了中国文学和民间传说中的经典角色，具有很高的艺术价值和文化内涵。
        """,
        user_name="唐三藏",
    )

    messages : List[TextMsg] = [
        TextMsg(role="assistant", content="让我杀了这三人吧，师傅？"),
    ]

    for i in range(1, 10):
        response = "".join(get_characterglm_response(messages, meta=character_meta))
        role = i % 2 == 0 and "assistant" or "user"
        print(f"{role}: {response}")
        messages.append(TextMsg(role=role, content=response))

    with open("output.txt", "w", encoding="utf-8") as f:
        for msg in messages:
            f.write(f"{msg['role']}: {msg['content']}\n")
    # for chunk in get_characterglm_response(messages, meta=character_meta):
    #     print(chunk)
    #     time.sleep(0.5)


if __name__ == "__main__":
    characterglm_example()
