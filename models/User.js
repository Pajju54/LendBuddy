import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    phone: {
        type: String,
        required: false
    },
    address: {
        type: String,
        required: false
    },
    dateJoined: {
        type: Date,
        default: Date.now
    },
    role: {
        type: String,
        enum: ['user', 'bank'],
        required: true
    }
});

export default mongoose.model('User', UserSchema);