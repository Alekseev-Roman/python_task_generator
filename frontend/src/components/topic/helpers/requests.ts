import axios from "axios";

export const fetchTopicName = async (id: any) => {
    const data = await axios
        .get(`/backend/get-topic-name-by-id?topic-id=${id}`)
    return data.data
}

export const fetchTasksByTopic = async (id: any) => {
    const data = await axios
        .get(`/backend/get-tasks-by-topic?topic-id=${id}`)
    return data.data
}

export const deleteTopic = async (id: any) => {
    await axios.post(`/backend/delete-topic?topic-id=${id}`)
}

export const deleteTask = async (id: any) => {
    await axios.post(`/backend/delete-task?task-id=${id}`)
}
