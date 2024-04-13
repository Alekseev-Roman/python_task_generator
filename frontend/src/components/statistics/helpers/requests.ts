import axios from "axios";

export const fetchStatistic = async () => {
        const data = await axios
            .get(`/backend/get-statistic`)
        return data.data
    }