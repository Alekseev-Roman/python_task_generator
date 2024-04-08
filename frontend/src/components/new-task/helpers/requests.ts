import axios from "axios";

export const downloadData = ( file: any ) => {
    const formData = new FormData()
    formData.append('data', file)
}

export const addTopic = async (topic_name: string) => {
    await axios.post(`/backend/import-new-topic?topic=${topic_name}`)
}

export const checkTopicInDB = async (topic_name: string) => {
    const data = await axios
        .get(`/backend/check-topic-in-db?topic=${topic_name}`)
    return data.data
}

export const fetchQuantityTask = async (topic_id: any, difficulty: any) => {
    return 0
}
