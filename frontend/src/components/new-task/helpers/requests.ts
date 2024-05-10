import axios from "axios";

export const downloadData = ( file: any, topic_id: any, difficulty: any) => {
    const formData = new FormData()
    formData.append('data', file)
    return axios
        .post(`/backend/import-task-from-file?topic=${topic_id}&difficulty=${difficulty}`,
            formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
    return axios.get(`/backend/import-task-from-file`)
}

export const addTopic = async (topic_name: string) => {
    await axios.post(`/backend/import-new-topic?topic=${topic_name}`)
}

export const checkTopicInDB = async (topic_name: string) => {
    const data = await axios
        .get(`/backend/check-topic-in-db?topic=${topic_name}`)
    return data.data
}

export const checkNameInDB = async (task_name: string) => {
    const data = await axios
        .get(`/backend/check-name-in-db?name=${task_name}`)
    return data.data
}

export const fetchQuantityTask = async (topic_id: any, difficulty: any)=> {
    const data = await axios
        .get(`/backend/get-quantity-tasks-topic-diff?difficulty=${difficulty}
        &topic=${topic_id}`)
    return data.data
}

export const importTask = async (task: object) => {
    return await (await axios.post('/backend/import-new-task', task)).data
}

export const importTaskByUrl = async (
    topic_id: any, difficulty: any, url: string
) => {
    await axios.post(
        `/backend/import-new-task-by-url?difficulty=${difficulty}
        &topic=${topic_id}`, {'url': url}
    )
}
