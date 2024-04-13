export interface Topic {
  _id: string
  name: string
}

export interface Task {
  task_id: number
  question_name: string
  question_text: string
}

export interface Coderunner {
  _id: string
  name: string
}

export interface MultichoiceAnswer {
  _id: number
  answer_fraction: number
  answer: string
}

export interface CoderunnerAnswer {
  _id: number
  example: string
  test_code: string
  expected: string
  use_as_example: boolean

}
