export interface Topic {
  _id: string
  name: string
}

export interface Task {
  task_id: number
  question_name: string
  question_text: string
}

export interface MultichoiceAnswer {
  _id: number
  answer_fraction: number
  answer: string
}

export interface CoderunnerTypes {
  _id: number
  name: string
}

export interface CoderunnerAnswer {
  _id: number
  example: string
  input: string
  result: string
  use_as_example: boolean

}
