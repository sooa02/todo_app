import streamlit as st

st.title('To-do App')

# (할 일 + 달성 여부) 객체로 관리하기 위해 만든 클래스
class Todo:
    print('클래스 언제?')
    def __init__(self, task: str, done: bool = False):
        self.__task = task
        self.__done = done

    def get_task(self):
        return self.__task

    def get_done(self):
        return self.__done

    def set_done(self, done: bool):
        self.__done = done

    # def __str__(self):
    #     return f'Task: {self.__task}, Done: {self.__done}'

    # 객체가 리스트 안에 있을 때 리스트 안의 요소들을 출력하려면 __repr__을 사용해야 출력됨
    # __str__ 사용할 경우 __repr__만 출력됨
    def __repr__(self):
        return f'Task: {self.__task}, Done: {self.__done}'

        # repr은 eval()로 다시 객체로 바꿀 수 있는 문자열 형태로 작성하는 게 원칙
        # return f'Todo(task="{self.task}", done={self.done})'
        # return f'Todo(task={self.task!r}, done={self.done})'

# __repr__ 심화 설명
# todo = Todo('숙제하기')
# print(id(todo))
# todo2 = eval(repr(todo))
# print(id(todo2))

# Todo 객체를 리스트에 쌓는 용도의 함수 (추가 할 일을 작성하면 실행되는 함수)
def add_todo():
    print(f'함수가 호출될 때 주머니에 담긴 값: {st.session_state.new_task}')
    todo = Todo(st.session_state.new_task)
    # print(todo)
    st.session_state.todos.append(todo)
    print(st.session_state['todos']) # list를 출력하면 __str__은 주소값, __repr__은 Todo 객체의 문자열로 구성되어 나옴
    st.session_state.new_task = ""

def togle_done(index: int):
    todo = st.session_state.todos[index]
    todo.set_done(not todo.get_done())


# todos (todo 객체를 담을 리스트를 초기화)
if 'todos' not in st.session_state:
    print('실행하자마자?')
    st.session_state.todos = []

# key 속성을 사용하면 key에 적힌 이름으로 사용자가 입력한 값이 session_state에 저장됨 (session_state에 새로운 키 초기화)
st.text_input('새로운 할일 추가', key='new_task', on_change=add_todo) # input 창에 내용을 작성(기존과 다른 내용)하고
                                                                        # 엔터하면 add_todo 함수 호출

if st.session_state.todos:
    print('몇 번째?')
    for i, todo in enumerate(st.session_state.todos):
        # st.write(f'{i+1}번째 todo -> {todo}')'
        col1, col2 =st.columns([0.1,0.9]) # [1:9] 비율 2로 하면 그냥 이등분
        col1.checkbox(f'{i+1}', value=todo.get_done(), key=f'done_{i}', on_change=togle_done, args=(i, ))
        col2.markdown(f'~~{todo.get_task()}~~' if todo.get_done() else todo.get_task())

else:
    st.info('할 일을 추가해 보세요.')
