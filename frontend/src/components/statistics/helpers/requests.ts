import axios from "axios";

export const fetchStatistic = async () => {
    const data = await axios
        .get(`/backend/get-statistic`)

    const statistic = []
    for (const topic in data.data) {
        statistic.push({
            topic_id: data.data[topic].topic_id,
            topic_name: data.data[topic].topic_name,
            quantity: data.data[topic].quantity,
            type_id: data.data[topic].type_id,
            type_name: data.data[topic].type_name,

        })
    }
    return statistic
}