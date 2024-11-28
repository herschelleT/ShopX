import React, { useState, useEffect } from 'react';
import axios from '../api/axios';

const Dashboard = () => {
    const [phones, setPhones] = useState([]);
    const [formData, setFormData] = useState({
        brand: '',
        model: '',
        ram: '',
        storage: '',
        camera: '',
        screen_size: '',
        battery_capacity: '',
        battery_rating: '',
        price: '',
        stock: ''
    });

    useEffect(() => {
        fetchPhones();
    }, []);

    const fetchPhones = async () => {
        try {
            axios.get('/phones').then((res) => {
                console.log(res.data);
                setPhones(res.data)
                
            });
            // console.log(response);
            
            // setPhones(response.data);
        } catch (error) {
            console.error('Error fetching phones:', error);
        }
    };

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('/phones', formData);
            fetchPhones(); // Refresh phone list after adding new entry
            setFormData({
                brand: '',
                model: '',
                ram: '',
                storage: '',
                camera: '',
                screen_size: '',
                battery_capacity: '',
                battery_rating: '',
                price: '',
                stock: ''
            });
        } catch (error) {
            console.error('Error adding phone:', error);
        }
    };

    const handleDelete = async (id) => {
        try {
            await axios.delete(`/phones/${id}`);
            fetchPhones(); // Refresh the list after deletion
        } catch (error) {
            console.error('Error deleting phone:', error);
        }
    };

    return (
        <div className="container px-3 mx-5">
            <h2 className="mb-4">Phone Dashboard</h2>
            <form onSubmit={handleSubmit} className="border p-4 mb-4 shadow-sm bg-light rounded">
                <div className="row mb-3">
                    <div className="col-md-6">
                        <input type="text" name="brand" placeholder="Brand" value={formData.brand} onChange={handleChange} className="form-control" required />
                    </div>
                    <div className="col-md-6">
                        <input type="text" name="model" placeholder="Model" value={formData.model} onChange={handleChange} className="form-control" required />
                    </div>
                </div>
                <div className="row mb-3">
                    <div className="col-md-4">
                        <input type="number" name="ram" placeholder="RAM (GB)" value={formData.ram} onChange={handleChange} className="form-control" />
                    </div>
                    <div className="col-md-4">
                        <input type="number" name="storage" placeholder="Storage (GB)" value={formData.storage} onChange={handleChange} className="form-control" />
                    </div>
                    <div className="col-md-4">
                        <input type="number" name="camera" placeholder="Camera (MP)" value={formData.camera} onChange={handleChange} className="form-control" />
                    </div>
                </div>
                <div className="row mb-3">
                    <div className="col-md-4">
                        <input type="number" step="0.1" name="screen_size" placeholder="Screen Size (inches)" value={formData.screen_size} onChange={handleChange} className="form-control" />
                    </div>
                    <div className="col-md-4">
                        <input type="number" name="battery_capacity" placeholder="Battery Capacity (mAh)" value={formData.battery_capacity} onChange={handleChange} className="form-control" />
                    </div>
                    <div className="col-md-4">
                        <select name="battery_rating" value={formData.battery_rating} onChange={handleChange} className="form-select">
                            <option value="">Select Battery Rating</option>
                            <option value="Average">Average</option>
                            <option value="Good">Good</option>
                            <option value="Excellent">Excellent</option>
                        </select>
                    </div>
                </div>
                <div className="row mb-3">
                    <div className="col-md-6">
                        <input type="number" step="0.01" name="price" placeholder="Price" value={formData.price} onChange={handleChange} className="form-control" required />
                    </div>
                    <div className="col-md-6">
                        <input type="number" name="stock" placeholder="Stock" value={formData.stock} onChange={handleChange} className="form-control" />
                    </div>
                </div>
                <button type="submit" className="btn btn-primary w-100">Add Phone</button>
            </form>

            <table className="table table-striped table-bordered table-hover mt-4">
                <thead className="table-dark">
                    <tr>
                        <th>Brand</th>
                        <th>Model</th>
                        <th>RAM</th>
                        <th>Storage</th>
                        <th>Camera</th>
                        <th>Screen Size</th>
                        <th>Battery Capacity</th>
                        <th>Battery Rating</th>
                        <th>Price</th>
                        <th>Average Rating</th>
                        <th>Wishlists</th>
                        {/* <th>Stock</th> */}
                    </tr>
                </thead>
                <tbody>
                    {phones?.map((phone) => (
                        <tr key={phone.id}>
                            <td>{phone.brand}</td>
                            <td>{phone.model}</td>
                            <td>{phone.ram} GB</td>
                            <td>{phone.storage} GB</td>
                            <td>{phone.camera} MP</td>
                            <td>{phone.screen_size} inches</td>
                            <td>{phone.battery_capacity} mAh</td>
                            <td>{phone.battery_rating}</td>
                            <td>${phone.price}</td>
                            <td>{phone.average_rating}</td>
                            <td>{phone.order_count}</td>
                            {/* <td>{phone.stock}</td> */}
                            <td>
                                <button onClick={() => handleDelete(phone.id)} className="btn btn-danger btn-sm">
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Dashboard;
