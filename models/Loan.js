import mongoose from 'mongoose';

const LoanSchema = new mongoose.Schema({
    borrower: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true
    },
    fullName: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true
    },
    phone: {
        type: String,
        required: true
    },
    loanType: {
        type: String,
        required: true,
        enum: ['personal', 'home', 'car', 'education', 'business']
    },
    loanAmount: {
        type: Number,
        required: true,
        min: 10000,
        max: 10000000
    },
    loanTenure: {
        type: Number,
        required: true,
        min: 3,
        max: 360
    },
    maxInterestRate: {
        type: Number,
        required: true,
        min: 5,
        max: 24
    },
    monthlyIncome: {
        type: Number,
        required: true
    },
    employmentType: {
        type: String,
        required: true
    },
    purpose: {
        type: String,
        required: true
    },
    status: {
        type: String,
        default: 'pending',
        enum: ['pending', 'approved', 'rejected']
    },
    offers: [
        {
            bank: {
                type: mongoose.Schema.Types.ObjectId,
                ref: 'User'
            },
            interestRate: {
                type: Number,
                required: true
            },
            approved: {
                type: Boolean,
                default: false
            },
            createdAt: {
                type: Date,
                default: Date.now
            }
        }
    ],
    createdAt: {
        type: Date,
        default: Date.now
    }
});

export default mongoose.model('Loan', LoanSchema);